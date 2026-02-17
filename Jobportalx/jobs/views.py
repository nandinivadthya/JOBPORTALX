from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from .utils import extract_text_from_pdf, calculate_resume_score


def home(request):
    jobs = Job.objects.all()
    return render(request, "home.html", {"jobs": jobs})


def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        user_type = request.POST.get("user_type", "employee")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not email or not password or not password2:
            messages.error(request, "Please fill all required fields.")
            return render(request, "register.html")
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")
        if User.objects.filter(username=email).exists():
            messages.error(request, "A user with that email already exists.")
            return render(request, "register.html")

        try:
            # Create user with is_staff=True if recruiter
            is_recruiter = user_type == "recruiter"
            user = User.objects.create_user(
                username=email, 
                email=email, 
                password=password,
                is_staff=is_recruiter
            )
            
            # Set full name
            if full_name:
                parts = full_name.split(None, 1)
                user.first_name = parts[0]
                if len(parts) > 1:
                    user.last_name = parts[1]
                user.save()
            
            # Login the user directly
            login(request, user)
            user_type_label = "Recruiter" if is_recruiter else "Job Seeker"
            messages.success(request, f"Welcome to JobPortalX! 🎉 Account created as {user_type_label}.")
            
            # Redirect to appropriate dashboard
            if is_recruiter:
                return redirect("recruiter_dashboard")
            else:
                return redirect("employee_dashboard")
                
        except IntegrityError as e:
            messages.error(request, "A user with that email already exists.")
            return render(request, "register.html")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.get_full_name() or user.username}! 👋")
            
            # Check for new accepted applications to notify job seeker
            if not user.is_staff:
                new_acceptances = Application.objects.filter(user=user, status='accepted', notified=False)
                for app in new_acceptances:
                    messages.success(request, f"Your application for {app.job.title} at {app.job.company} has been accepted! 🎊")
                    app.notified = True
                    app.save()
                    
            if user.is_staff:
                return redirect("recruiter_dashboard")
            else:
                return redirect("employee_dashboard")
        messages.error(request, "Invalid email or password.")
        return render(request, "login.html")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def employee_dashboard(request):
    # Get all jobs except user's own applications
    jobs = Job.objects.all().prefetch_related('applications')
    user_applications = Application.objects.filter(user=request.user)
    applied_job_ids = user_applications.values_list('job_id', flat=True)
    
    # Get user's applications
    my_applications = user_applications.select_related('job')
    
    context = {
        'jobs': jobs,
        'applied_job_ids': list(applied_job_ids),
        'my_applications': my_applications,
    }
    return render(request, "employee_dashboard.html", context)


@login_required
def recruiter_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, "You don't have access to recruiter dashboard.")
        return redirect("home")
    
    # Get jobs posted by this recruiter
    my_jobs = Job.objects.filter(recruiter=request.user)
    
    # Get all applications for recruiter's jobs
    applications = Application.objects.filter(job__recruiter=request.user).select_related('user', 'job')
    
    context = {
        'my_jobs': my_jobs,
        'applications': applications,
    }
    return render(request, "recruiter_dashboard.html", context)


@login_required
def upload_job(request):
    if not request.user.is_staff:
        messages.error(request, "Only recruiters can upload jobs.")
        return redirect("home")
    
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect("recruiter_dashboard")
    else:
        form = JobForm()
    
    return render(request, "upload_job.html", {"form": form})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if job.recruiter != request.user:
        messages.error(request, "You can only edit your own jobs.")
        return redirect("recruiter_dashboard")
    
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully!")
            return redirect("recruiter_dashboard")
    else:
        form = JobForm(instance=job)
    
    return render(request, "edit_job.html", {"form": form, "job": job})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if job.recruiter != request.user:
        messages.error(request, "You can only delete your own jobs.")
        return redirect("recruiter_dashboard")
    
    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect("recruiter_dashboard")
    
    return render(request, "confirm_delete_job.html", {"job": job})


@login_required
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    # Check if already applied
    if Application.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect("employee_dashboard")
    
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect("employee_dashboard")
    else:
        form = ApplicationForm()
    
    return render(request, "apply_job.html", {"form": form, "job": job})


@login_required
def view_applicants(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if job.recruiter != request.user:
        messages.error(request, "You don't have access to this job's applications.")
        return redirect("recruiter_dashboard")
    
    applications = job.applications.all().select_related('user')
    
    return render(request, "view_applicants.html", {"job": job, "applications": applications})


@login_required
def update_application_status(request, application_id, status):
    application = get_object_or_404(Application, id=application_id)
    
    if application.job.recruiter != request.user:
        messages.error(request, "You don't have permission to update this application.")
        return redirect("recruiter_dashboard")
    
    if status in ['accepted', 'rejected', 'pending']:
        application.status = status
        application.save()
        messages.success(request, f"Application status updated to {status}!")
    
    return redirect("view_applicants", job_id=application.job.id)


@login_required
def view_application_details(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    
    if application.job.recruiter != request.user and application.user != request.user:
        messages.error(request, "You don't have access to this application.")
        return redirect("home")
    
    
    resume_score = None
    if application.resume:
        try:
            resume_path = application.resume.path
            resume_text = extract_text_from_pdf(resume_path)
            job_description = application.job.description
            score_data = calculate_resume_score(resume_text, job_description)
            resume_score = score_data['score']
            matched_keywords = score_data['matched_keywords']
        except Exception as e:
            print(f"Error calculating resume score: {e}")
            
    return render(request, "view_application_details.html", {
        "application": application, 
        "resume_score": resume_score,
        "matched_keywords": matched_keywords
    })


from django.http import FileResponse, Http404
import os

@login_required
def serve_resume(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    
    # Permission check
    if application.job.recruiter != request.user and application.user != request.user:
        messages.error(request, "You don't have access to this application.")
        return redirect("home")
    
    if not application.resume:
        raise Http404("Resume not found")
        
    try:
        # Open the file
        file_path = application.resume.path
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        
        # Set headers to allow embedding
        # We explicitly remove restrictive headers or set them to allow embedding
        response['X-Frame-Options'] = 'SAMEORIGIN' # Or remove it entirely if SAMEORIGIN is still problematic, but SAMEORIGIN should work. 
        # Actually, let's remove it to be safe if the middleware is adding it.
        # But middleware adds it at the end. We might need to use @xframe_options_exempt decorator if middleware is strict.
        
        # Let's try setting it to SAMEORIGIN first, as that is what we want. 
        # But wait, middleware *already* sets it to SAMEORIGIN. The issue might be COOP.
        
        response['Content-Disposition'] = 'inline; filename="{}"'.format(os.path.basename(file_path))
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none' # Relax this
        return response
    except FileNotFoundError:
        raise Http404("Resume file missing on server")
