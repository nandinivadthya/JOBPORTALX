# JobPortalX Setup & Usage Guide

## Overview

JobPortalX is now a complete job portal system with two main user roles:

- **Job Seekers (Employees)**: Browse and apply for jobs
- **Recruiters (Hiring Managers)**: Post jobs and manage applications

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt doesn't exist, install:

```bash
pip install django
```

### 2. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a Superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 4. Run the Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## Features Overview

### For Job Seekers (Employees)

#### 1. **Registration**

- Navigate to `/register/`
- Select "Job Seeker (Employee)" as user type
- Complete registration

#### 2. **Dashboard**

- View all available jobs in a card grid
- Apply for jobs (if not already applied)
- View your application history
- Track application status (Pending, Accepted, Rejected)

#### 3. **Job Application**

- Click "Apply Now" on any job card
- Optionally add a cover letter
- Submit application

#### 4. **Application Status Tracking**

- View all your applications in the "My Applications" tab
- See current status for each application
- View application details

---

### For Recruiters (Hiring Managers)

#### 1. **Registration**

- Navigate to `/register/`
- Select "Recruiter (Hiring Manager)" as user type
- Complete registration

#### 2. **Dashboard**

- Overview of:
  - Total jobs posted
  - Total applications received
  - Accepted applications

#### 3. **Post a Job**

- Click "+ Post New Job"
- Fill in job details:
  - Job Title
  - Company Name
  - Location
  - Salary (Annual)
  - Job Description
- Submit to publish

#### 4. **Manage Posted Jobs**

- View all your posted jobs
- See application count for each job
- **Edit Job**: Update job details
- **Delete Job**: Remove a job posting
- **View Applicants**: See all applications for a specific job

#### 5. **Manage Applications**

- View all applications across all your jobs
- **View Applicants**: See candidates for specific jobs
- **View Application Details**: Read cover letters and candidate info
- **Accept/Reject Applications**: Update application status

---

## User Workflows

### Job Seeker Workflow

1. Register → Select "Employee"
2. Go to Dashboard
3. Browse available jobs in "Available Opportunities" tab
4. Click "Apply Now" → Add cover letter (optional) → Submit
5. Track application in "My Applications" tab
6. View application details for status updates

### Recruiter Workflow

1. Register → Select "Recruiter"
2. Click "+ Post New Job"
3. Fill job details and publish
4. View applications in "All Applications" tab
5. Click "View Applicants" to see applications for specific jobs
6. Accept or reject applications
7. View application details including cover letters

---

## URL Routes

### Public Routes

- `/` - Home page with all jobs
- `/login/` - User login
- `/register/` - User registration

### Employee Routes

- `/employee/dashboard/` - Employee dashboard
- `/apply/job/<job_id>/` - Apply for a job
- `/view/application/<app_id>/` - View application details

### Recruiter Routes

- `/recruiter/dashboard/` - Recruiter dashboard
- `/upload/job/` - Post a new job
- `/edit/job/<job_id>/` - Edit a job
- `/delete/job/<job_id>/` - Delete a job
- `/view/applicants/<job_id>/` - View applicants for a job
- `/update/application/<app_id>/<status>/` - Update application status
- `/view/application/<app_id>/` - View application details

### Common Routes

- `/logout/` - Logout

---

## Admin Panel

Access admin at: http://127.0.0.1:8000/admin/

### Manage:

- **Jobs**: View, create, edit, delete job postings
- **Applications**: View, filter, and manage applications
- **Users**: Manage user accounts

---

## Database Models

### Job Model

```
- title (CharField)
- company (CharField)
- location (CharField)
- salary (IntegerField)
- description (TextField)
- recruiter (ForeignKey to User)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Application Model

```
- user (ForeignKey to User - Job seeker)
- job (ForeignKey to Job)
- applied_date (DateTimeField)
- status (CharField - pending/accepted/rejected)
- cover_letter (TextField)
- unique_together (user, job) - Prevents duplicate applications
```

---

## Features Implemented

✅ User registration with role selection (Employee/Recruiter)
✅ Job posting by recruiters
✅ Job browsing by employees
✅ Job application with cover letter support
✅ Application status tracking (Pending, Accepted, Rejected)
✅ Recruiter dashboard for job management
✅ Employee dashboard for job search and applications
✅ View applicants functionality
✅ Application history tracking
✅ Clean, responsive UI
✅ Admin panel for system management

---

## Testing Guide

### Test Account Creation

1. **As an Employee:**
   - Go to /register
   - Name: John Doe
   - Email: employee@test.com
   - Password: test123
   - User type: Job Seeker

2. **As a Recruiter:**
   - Go to /register
   - Name: Jane Recruiter
   - Email: recruiter@test.com
   - Password: test123
   - User type: Recruiter

### Post a Test Job (as Recruiter)

1. Login as recruiter
2. Click "+ Post New Job"
3. Fill details:
   - Title: Python Developer
   - Company: TechCorp
   - Location: Bangalore
   - Salary: 600000
   - Description: We are looking for...
4. Submit

### Apply for a Job (as Employee)

1. Login as employee
2. Go to Dashboard
3. View available jobs
4. Click "Apply Now"
5. Add cover letter (optional)
6. Submit application

### Track Application (as Recruiter)

1. Go to Recruiter Dashboard
2. Click "View Applicants" for the job
3. View applicant details
4. Accept or Reject application

---

## Notes

- Each user can only apply once per job (duplicate applications prevented)
- Recruiters can edit and delete their own jobs
- Application status defaults to "Pending" when submitted
- Admin can manage all jobs and applications
- Responsive design works on mobile and desktop

---

## Troubleshooting

**Migration Errors:**

```bash
python manage.py migrate --fake initial
python manage.py migrate
```

**Static files not loading:**

```bash
python manage.py collectstatic --noinput
```

**Clear database (reset everything):**

```bash
python manage.py flush
```

---

## Future Enhancements

- Email notifications for applications
- Candidate resume upload
- Interview scheduling
- Job bookmarking/favorites
- Advanced search filters
- Rating and review system
- Payment integration for premium listings
