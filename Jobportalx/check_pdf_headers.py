import urllib.request
from jobs.models import Application
import os
import sys
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

def check_headers():
    app = Application.objects.get(id=9)
    url = f"http://127.0.0.1:8000{app.resume.url}"
    print(f"Checking URL: {url}")
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print("--- Headers ---")
            for k, v in response.headers.items():
                print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_headers()
