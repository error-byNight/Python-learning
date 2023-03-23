##returns a list of all the vowels in the string

def find_vowels(s):
    vowels = ['a','e','i','o','u']
    result = []
    for latter in s:
        if latter.lower() in vowels:
            result.append(latter)
            
    return result

        
input_string = input("Enter the String : ")        
result = find_vowels(input_string)        
print(result)
        
            
