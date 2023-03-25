import random

while True:
    choice = ["rock","paper","scissor"]
    print("Your Choice","rock=1","paper=2","scissor=3")

    computerChoice = random.randint(1,3)
    userChoice = int(input("Enter your Choice :"))

    print(computerChoice)
    print("Computer Choice : ", choice[computerChoice - 1])

    if (computerChoice == userChoice):
        print("Match Tie")

    elif ((computerChoice == 1 and userChoice == 3) or (computerChoice == 2 and userChoice == 1) or (computerChoice == 3 and userChoice == 2)):
        print("Computer Wins","You Lost")

    else:
        print("You Won")
        
    print("--------------------------------------------------------------------------------------------------------")        

