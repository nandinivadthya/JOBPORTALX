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
    print(f"Checking {url}")
    
    output_file = "header_debug_output.txt"
    
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            with open(output_file, "w") as f:
                f.write(f"Url: {url}\n")
                f.write(f"Status: {response.status}\n")
                f.write("Headers:\n")
                for k, v in response.headers.items():
                    f.write(f"{k}: {v}\n")
        print(f"Headers written to {output_file}")
    except Exception as e:
        with open(output_file, "w") as f:
            f.write(f"Error: {e}\n")
        print(f"Error checking headers: {e}")

if __name__ == "__main__":
    check()
