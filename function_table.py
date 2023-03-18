##Writing table using function

##Define Function
def table(userTable) :
    for i in range (1,11):
        print(str(userTable) , "X" , str(i) , "="  , str(userTable * i))
        


##calling Function
userInput = int(input("Which numbers table you want :"))
table(userInput)
