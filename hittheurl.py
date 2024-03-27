import requests

def hit_url(url, num_requests):
    for i in range(num_requests):
        response = requests.get(url)
        print(f"Request {i+1}: Status code - {response.status_code}")

if __name__ == "__main__":
    url = input("Enter the URL you want to hit: ")
    num_requests = int(input("Enter the number of times you want to hit the URL: "))

    hit_url(url, num_requests)
    https://justsocial.co.in/