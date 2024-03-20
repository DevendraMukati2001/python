# stone paper scissors
import random
import time

print("choose S for stone P for paper x for scissors\nuse capital letters\n")
n=int(input("how many rounds you want to play?\n"))

you = int(0)
com = int(0)

for i in range(1,n+1):

    OPTIONS = ["stone", "paper", "scissors"]
    user = input("your choice:")
    sun = random.choice(OPTIONS)
    print("computer 's choice:",sun)
    if user == "S" and sun == OPTIONS[0]:
        print("its a draw.\nNO POINTS")
    elif user == "P" and sun == OPTIONS[1]:
        print("its a draw.\nNO POINTS")
    elif user == "X" and sun == OPTIONS[2]:
        print("its a draw.\nNO POINTS")
    elif user == "S" and sun == OPTIONS[1]:
        print("you lost \n zero points")
        com = com + 1
    elif user == "P" and sun == OPTIONS[0]:
        print("you won\n plus one")
        you = you + 1
    elif user == "S" and sun == OPTIONS[2]:
        print("you won \n plus one")
        you = you + 1
    elif user == "X" and sun == OPTIONS[0]:
        print("you lost\n zero points")
        com = com + 1
    elif user == "P" and sun == OPTIONS[2]:
        print("you lost \n zero points")
        com = com + 1
    elif user == "X" and sun == OPTIONS[1]:
        print("you won\n plus one")
        you = you + 1

print("\nso final scores are")
time.sleep(2)
print("your scores:\t", you, "\nyour opponent scores:\t", com)
if you > com:
    print("you won")
elif com > you:
    print("you lost")
elif you == com:
    print("its a draw")
print("GAME OVER")
