num_list = input("Enter a list of number separated by space : ").split()
sum = 0
for num in num_list:
    sum += int(num)
    avg = sum / len(num_list)

print("Sum :", sum)

print("Average :",avg)
