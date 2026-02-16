from django import forms
from .models import Job, Application


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Location'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Job Description'}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your cover letter here...', 'required': False}),
            'resume': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx', 'required': False}),
        }
