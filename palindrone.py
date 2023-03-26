def palindrome(string):
    """
    Returns True if the given string is a palindrome, False otherwise.
    Ignores spaces, punctuation, and capitalization.
    """
    # Convert the string to lowercase and remove spaces and punctuation
    string = ''.join(char for char in string.lower() if char.isalnum())
    
    # Compare the original string to its reverse and return True if they are the same
    return string == string[::-1]

print(palindrome("racecar"))   # True
print(palindrome("level"))     # True
print(palindrome("A man, a plan, a canal, Panama!"))   # True
print(palindrome("hello"))     # False 

