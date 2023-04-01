# Define the introduction to the game
print('''Welcome to the adventure game! You find yourself standing
in front of a castle.''')

# Define a function for the first location
def castle_gates():
    print('''You are standing in front of the castle gates.
What would you like to do? ''')
    choice = input("Enter '1' to open the gates, '2' to climb the wall, or '3' to turn back: ")
    if choice == '1':
        print("You try to open the gates, but they are locked. You will need to find a key.")
        castle_gates() # loop back to the same function
    elif choice == '2':
        print("You attempt to climb the wall, but it's too high. You need to find another way.")
        castle_gates() # loop back to the same function
    elif choice == '3':
        print("You turn back and leave the castle.")
    else:
        print("Invalid choice. Please try again.")
        castle_gates() # loop back to the same function

# Call the first location function to start the game
castle_gates()
