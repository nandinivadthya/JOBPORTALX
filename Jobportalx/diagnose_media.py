import os
import django
import sys
import urllib.request
from pathlib import Path

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

from jobs.models import Application
from django.conf import settings

def diagnose():
    print("--- Diagnostics ---")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"MEDIA_URL: {settings.MEDIA_URL}")
    
    try:
        app = Application.objects.get(id=9)
        print(f"Application ID: {app.id}")
        
        if not app.resume:
            print("No resume file associated.")
            return

        print(f"Resume Field: {app.resume}")
        print(f"Resume URL: {app.resume.url}")
        
        try:
            # Check file existence
            file_path = app.resume.path
            print(f"Resume Path from model: {file_path}")
            if os.path.exists(file_path):
                print(f"File EXISTS at {file_path}")
            else:
                print(f"File MISSING at {file_path}")
                # Check directly in media root
                direct_path = os.path.join(settings.MEDIA_ROOT, app.resume.name)
                print(f"Checking direct path: {direct_path}")
                if os.path.exists(direct_path):
                    print("File found at direct path.")
                else:
                    print("File also missing at direct path.")
        except Exception as e:
             print(f"File path check failed: {e}")

        # Check reachability
        url = f"http://127.0.0.1:8000{app.resume.url}"
        print(f"Testing URL: {url}")
        try:
            with urllib.request.urlopen(url) as response:
                print(f"Status Code: {response.getcode()}")
                print(f"Headers: {response.info()}")
        except urllib.error.HTTPError as e:
             print(f"HTTP Error: {e.code} {e.reason}")
        except urllib.error.URLError as e:
             print(f"URL Error: {e.reason}")
        except Exception as e:
            print(f"Request failed: {e}")

    except Application.DoesNotExist:
        print("Application 9 not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    diagnose()
