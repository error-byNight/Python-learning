def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Prompt the user to enter a temperature and its unit of measure
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of measure (C/F): ")

# Convert the temperature to the opposite unit of measure
if unit == "C":
    converted_temp = celsius_to_fahrenheit(temperature)
    new_unit = "F"
elif unit == "F":
    converted_temp = fahrenheit_to_celsius(temperature)
    new_unit = "C"
else:
    print("Error: Invalid unit of measure.")
    exit()

# Display the converted temperature
print(f"{temperature} {unit} = {converted_temp:.1f} {new_unit}")

