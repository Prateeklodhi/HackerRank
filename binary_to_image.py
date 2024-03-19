import os
import requests

def fetch_binary_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Get the binary content
            binary_data = response.content
            return binary_data
        else:
            print("Failed to fetch binary data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def save_binary_to_file(binary_data, file_name):
    try:
        # Write the binary data to a file in the current directory
        with open(file_name, 'wb') as f:
            f.write(binary_data)
        print("Binary data saved to file:", file_name)
    except Exception as e:
        print("An error occurred while saving binary data to file:", e)

if __name__ == "__main__":
    # Replace 'url' with the actual URL from which you want to fetch the binary data
    url = 'src="https://sprezzy.in/files/storage/64/149065ee062476b9d1710097956gk96xiaozdz9oyj6ddfp.jpeg"'
    binary_image_data = fetch_binary_from_url(url)
    
    if binary_image_data:
        # Save the binary data to a file in the current directory
        save_binary_to_file(binary_image_data, 'image.jpg')
    else:
        print("Failed to fetch binary image data.")
