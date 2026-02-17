import urllib.request

try:
    url = "http://127.0.0.1:8000/media/resumes/Nandhini_Resume_1.pdf"
    with urllib.request.urlopen(url) as response:
        with open("headers_output.txt", "w") as f:
            f.write(f"Status Code: {response.getcode()}\n")
            f.write(f"Content-Type: {response.headers.get('Content-Type')}\n")
            f.write(f"Content-Disposition: {response.headers.get('Content-Disposition')}\n")
            f.write("\nAll Headers:\n")
            for key, value in response.headers.items():
                f.write(f"{key}: {value}\n")
except Exception as e:
    with open("headers_output.txt", "w") as f:
        f.write(f"Error: {e}")
