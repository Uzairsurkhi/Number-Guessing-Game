import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice() to pick characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Default password length is 12 characters
    password = generate_password()
    print("Generated Password:", password)
