import requests

def check_https(url):
    """Check if the website is using HTTPS."""
    response = requests.head(url)
    if response.status_code == 200 and response.url.startswith("https://"):
        print("Website is using HTTPS.")
    else:
        print("Website may not be using HTTPS.")

def check_security_headers(url):
    """Check if the website has appropriate security headers."""
    response = requests.get(url)
    headers = response.headers
    security_headers = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options"]

    print("Security Headers:")
    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header} header is missing.")

def main():
    url = input("Enter the URL of the website you want to test: ")

    print("\nPerforming basic security checks...\n")
    check_https(url)
    check_security_headers(url)

if __name__ == "__main__":
    main()