from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary mapping emails to their hashed passwords
    password_to_check: the password we want to test alongside the email to login with
    """
    # Use .get() to avoid KeyError if email is not found
    return stored_logins.get(email) == hash_password(password_to_check)

# Hashing function (no need to modify)
def hash_password(password):
    """Takes in a password and returns the SHA256 hashed value."""
    return sha256(password.encode()).hexdigest()

def main():
    # Simulated stored logins (emails mapped to hashed passwords)
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    # Testing different login attempts
    test_cases = [
        ("example@gmail.com", "word"),           # Wrong password
        ("example@gmail.com", "password"),       # Correct password
        ("code_in_placer@cip.org", "Karel"),     # Correct password
        ("code_in_placer@cip.org", "karel"),     # Wrong password (case-sensitive)
        ("student@stanford.edu", "password"),    # Wrong password
        ("student@stanford.edu", "123!456?789"), # Correct password
        ("unknown@unknown.com", "password")      # Email not in stored_logins
    ]
    
    for email, password in test_cases:
        print(f"Login attempt for {email}: {'✅ Success' if login(email, stored_logins, password) else '❌ Failed'}")

if __name__ == '__main__':
    main()
