string = input("Enter a String :")
count =0
for char in string :
    if char.lower() in 'aeiou':
        count += 1
print(count)
