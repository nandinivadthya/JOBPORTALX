import os
import sys
import urllib.request
import django

# Add the project root to sys.path
# Assuming this script is located at d:\Jobportalx\JOBPORTALX\Jobportalx\check_headers_v2.py
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

from jobs.models import Application

def check():
    try:
        app = Application.objects.get(id=9)
        if not app.resume:
            print("No resume found for app 9")
            return
            
        url = f"http://127.0.0.1:8000{app.resume.url}"
        print(f"Checking {url}")
        
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print(f"Status: {response.status}")
            headers = response.info()
            print("Headers:")
            for k, v in headers.items():
                print(f"{k}: {v}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check()
