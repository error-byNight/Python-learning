input_list = [1,2,3,3,2,4,1,4,7,9,7]
unique_list = []

for num in input_list:
    if num not in unique_list:
        unique_list.append(num)
        
print("Lists are :", input_list)
print("Unique List are :" , unique_list)

    
