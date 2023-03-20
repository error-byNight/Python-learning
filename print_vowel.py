##Write a Python program that asks the user to input a string and
##then prints out the number of vowels in the string.
string = input("Enter a String : ")
vowel = ['a','e','i','o','u']
count = 0
for char in string:
    if char.lower() in vowel:
        count += 1
print("Total Number of Vowel in the Above String are : " ,count)
