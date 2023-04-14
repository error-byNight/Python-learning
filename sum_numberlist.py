def sum_numbers():
    numbers = input("Enter a List of numbers separated by spaces : ")
    numbers_list = numbers.split()
    total = 0
    for num in numbers_list:
        total += int(num)
    return total
print(sum_numbers())


