def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
text = input("Enter a String : ")
print(remove_vowels(text))  


