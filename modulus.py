# check if a number is even or odd
x = 10
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

print("-----------------------------------------")
# perform an operation on every other element of a list
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    if i % 2 == 0:
        my_list[i] = my_list[i] * 2
print(my_list)

