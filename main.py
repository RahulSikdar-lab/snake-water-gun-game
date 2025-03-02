'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
yourchoice = input("Enter you choice :")
youdict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake" , -1:"Water", 0: "gun"}

you = youdict[yourchoice]
print(f"your choice {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("it's a draw!")

else:
    if(computer == -1 and you ==1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer ==1 and you == -1):
        print("you lose!")
    
    elif(computer ==1 and you ==0):
        print("you win!")

    elif(computer == 0 and you ==-1):
        print("you win!")

    elif(computer ==0 and you ==1):
        print("you lose!")
    
    else:
        print("Something went wrong!")
