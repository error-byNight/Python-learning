##Write a Python program that generates a random number between 1 and 10
##and asks the user to guess the number.
##The program should give the user up to three chances to guess the number
##and should provide feedback on whether the guess is too high or too low.
##If the user guesses the correct number within three tries,
##the program should print a message congratulating the user.

import random
number = random.randint(1, 10)
tries = 0
while tries <3:
    guess = int(input("Enter the number between 1 to 10 :"))
    tries += 1
    if guess == number:
         print("Congrats you Guessed in" , tries, "tries .")
         break
    elif guess < number:
      print("You Guessed too low , Try Again .")
    else:
      print("You Guessed too high , Try Again.")
if tries == 3:
    print("You didn't guess the number . The number was " , number)
    
    
