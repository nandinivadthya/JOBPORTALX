from django.db import models
from django.contrib.auth.models import User

# Job Model
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    description = models.TextField()
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# Application Model
class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text='Upload your resume (PDF, DOC, DOCX)')

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

    class Meta:
        unique_together = ('user', 'job')
        ordering = ['-applied_date']


# Create your models here.

# Certification Model
class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField()
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

# Recruiter Connection Model
class RecruiterConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recruited_by')
    connected_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ↔ {self.recruiter.username}"
