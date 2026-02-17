import urllib.request
import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobportalx.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def check_endpoint():
    # We need to simulate a logged-in user since the view is login_required
    c = Client()
    
    # Get a user (assuming admin or user 1 exists and is staff/owner)
    try:
        user = User.objects.get(id=1) 
        c.force_login(user)
        print(f"Logged in as {user.username}")
    except User.DoesNotExist:
        print("User ID 1 not found, cannot test login required view easily without credentials.")
        return

    url = "/application/9/resume/"
    print(f"HEAD {url}")
    
    try:
        response = c.head(url)
        print(f"Status: {response.status_code}")
        print("Headers:")
        for k, v in response.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_endpoint()
