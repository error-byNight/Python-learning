def even_numbers():
    """
    Prompts the user to input a list of integers and prints a new list containing only the even numbers.
    """
    numbers = input("Enter a list of integers separated by spaces: ")
    numbers = [int(num) for num in numbers.split()]
    even_list = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_list)

even_numbers()
