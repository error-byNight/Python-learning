import random
import string

def generate_password(length):
    # Define all possible characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one special character in the password
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if any(c in string.punctuation for c in password):
            return password

# Get user input for password length
length = int(input("Enter desired password length: "))

# Generate password and print to console
password = generate_password(length)
print(f"Generated password: {password}")
