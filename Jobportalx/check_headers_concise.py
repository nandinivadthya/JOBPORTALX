import urllib.request
import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

from jobs.models import Application

def check():
    app = Application.objects.get(id=9)
    url = f"http://127.0.0.1:8000{app.resume.url}"
    print(f"HEAD {url}")
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print(f"Status: {response.status}")
            print("X-Frame-Options:", response.headers.get('X-Frame-Options', 'NOT SET'))
            print("Content-Security-Policy:", response.headers.get('Content-Security-Policy', 'NOT SET'))
            print("Content-Type:", response.headers.get('Content-Type', 'NOT SET'))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check()
