import os
import sys
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

from jobs.utils import calculate_resume_score, extract_text_from_pdf
from jobs.models import Application

def test_scoring():
    try:
        app = Application.objects.get(id=9)
        print(f"Testing App ID: {app.id}")
        
        if not app.resume:
            print("No resume found.")
            return

        print(f"Resume: {app.resume.path}")
        text = extract_text_from_pdf(app.resume.path)
        print(f"Extracted Text Length: {len(text)}")
        print(f"Preview: {text[:200]}...")
        
        job_desc = app.job.description
        print(f"Job Description Length: {len(job_desc)}")
        
        score = calculate_resume_score(text, job_desc)
        print(f"Calculated Score: {score}%")
        
    except Application.DoesNotExist:
        print("Application 9 not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_scoring()
