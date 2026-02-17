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
    print("--- Diagnostics V2 ---")
    try:
        app = Application.objects.get(id=9)
        print(f"Application ID: {app.id}")
        
        if not app.resume:
            print("No resume file associated.")
            return

        print(f"Resume Name (DB Value): '{app.resume.name}'")
        print(f"Resume URL: '{app.resume.url}'")
        print(f"Resume Path (Calculated): '{app.resume.path}'")

        # Check if path exists
        try:
            if os.path.exists(app.resume.path):
                if os.path.isdir(app.resume.path):
                     print("Path EXISTS but is a DIRECTORY.")
                else:
                     print("Path EXISTS and is a FILE.")
            else:
                print("Path does NOT exist on disk.")
        except Exception as e:
            print(f"Path check error: {e}")
            
        # Check URL reachability
        url = f"http://127.0.0.1:8000{app.resume.url}"
        print(f"Testing URL: {url}")
        
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req) as response:
                print(f"Status Code: {response.getcode()}")
                print(f"Content-Type: {response.headers.get('Content-Type')}")
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
