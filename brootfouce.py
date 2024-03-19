import random
import string

def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_lowercase + string.digits
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def save_string_to_file(string, file_name):
    try:
        # Write the string to a file
        with open(file_name, 'w') as f:
            f.write(string)
        print("String saved to file:", file_name)
    except Exception as e:
        print("An error occurred while saving string to file:", e)

if __name__ == "__main__":
    # Define the length of the random string
    length = 32
    file_data = ''
    # Generate a random string
    for item in range(0,100):
        random_string = generate_random_string(length)
        file_data = file_data + '\n' + random_string
    
    # Save the random string to a file
    save_string_to_file(file_data, 'random_string.txt')