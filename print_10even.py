##Write a program in Python that prints the first 10 even numbers,
##starting from 0.
i = 0
count = 0
while count < 10:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1
