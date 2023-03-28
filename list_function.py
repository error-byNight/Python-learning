my_list = [1, 2, 3]
my_list.append(4)
print("Apppend Function - ",my_list)
print("-------------------------------------------")
my_list = [1, 2, 3, 2]
my_list.remove(2)
print("Remove Function  - ",my_list)
print("-------------------------------------------")
my_list = [1, 2, 3, 2]
my_list.clear()
print("Clear Function   - ",my_list)
print("-------------------------------------------")
my_list = [1, 2, 3, 2, 2, 4]
x = my_list.count(2)
print("Count Function   - ",x)
print("-------------------------------------------")
my_list = [1, 2, 3, 4, 5]
my_copy = my_list.copy()
print("Copy Function    - ",my_copy)
print("-------------------------------------------")
my_list = [1, 2, 3, 2]
index_of_2 = my_list.index(2)
print("Index Function   - ",index_of_2)
print("-------------------------------------------")
print("Print Traverse Using While Loop:")
my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print("Treversing Function -",my_list[index])
    index += 1
print("-------------------------------------------")
string = "Hello, World!"
words = string.split(",")
print("Split Function   -",words)
print("-------------------------------------------")
print("Print Traverse Using for Loop:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print("Traverse Function",item)
print("-------------------------------------------")
def even_numbers():
    numbers = input("Enter a list of integers separated by spaces: ")
    numbers = [int(num) for num in numbers.split()]
    even_list = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_list)
even_numbers()
print("-------------------------------------------")
##WAP to print list number using Slice Method
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Slice Method",numbers[2:7:2])
print("Slice Method",numbers[4:10:2])
print("-------------------------------------------")
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]
for num in numbers:
    if num % 2 != 0:
        print(num)









