import re

def is_strong_password(password):
    """
    Checks if the given password is strong based on the following rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    """

    # Length
    if len(password) < 8:
        return False

    #  Check for any uppercase letters
    if not re.search(r'[A-Z]', password):
        return False

    # check for any lowercase letters
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one number
    if not re.search(r'[0-9]', password):
        return False

    
    return True


# Sample passwords to test but you can use any passwords to test these are just simple ones that meet the criteria 
sample_passwords = [
    "Password123",    
    "password",       
    "PASSWORD",       
    "Pass123",          
]

# Check each sample
for pwd in sample_passwords:
    result = is_strong_password(pwd)
    print(f"{pwd}: {'Strong' if result else 'Weak'}")