a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a+b
print("--------------------------")
print("--------------------------")
n = int(input("Enter the number of terms you want in the Fibonacci series: "))

# Initializing the first two terms
a, b = 0, 1

# Print the first n terms of the Fibonacci series
print("Fibonacci series:")
for i in range(n):
    print(a, end='  ,  ')
    a, b = b, a + b
