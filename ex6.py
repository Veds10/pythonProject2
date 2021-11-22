import random
lst=["paper","rock","scissors"]

i=0
while(i<=3):
    user=input("enter your choice paper rock scissors")
    comp=random.choice(lst)

    if user==comp:
        print("tie")

    elif user=="paper" and comp=="rock" :
        print("user is winner")


    elif user == "paper" and comp == "scissor":
        print("comp is winner")



    elif user == "scissor" and comp == "rock":
        print("comp is winner")



    elif user == "scissor" and comp == "paper":
        print("user is winner")


    elif user == "rock" and comp == "scissor":
        print("user is winner")


    elif user == "rock" and comp == "paper":
        print("comp is winner")

    else:
        print("invalid")

    i+=1

if i>=3:
    print("game over")


