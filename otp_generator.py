import random
import string

def generate_otp(length):
    """Generate an OTP of the specified length."""
    # Define possible characters to use in the OTP
    characters = string.ascii_letters + string.digits
    
    # Generate OTP by selecting random characters from the pool
    otp = ''
    for i in range(length):
        otp += random.choice(characters)
        
    return otp

def verify_otp(otp, input_otp):
    """Verify if the provided OTP is valid."""
    if otp == input_otp:
        return True
    else:
        return False

# Example usage
length = 6 # Length of OTP
otp = generate_otp(length)
print(f"Generated OTP: {otp}")

input_otp = input("Enter OTP: ")
if verify_otp(otp, input_otp):
    print("OTP is valid.")
else:
    print("Invalid OTP.")
