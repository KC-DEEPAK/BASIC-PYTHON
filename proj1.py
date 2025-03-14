# IT IS A GAME ROCK PAPER SCISSOR
#CONDITION ,PAPER WITH ROCK=PAPER WINS,ROCK WIN AGINEST A SCISSOR,SCISSOR WIN AGIANST A PAPER
#  TAKE ROCK =0,AND PAPER=1,SCISSOR=2;
import random
user=int(input("enter the condition you want to play.\n"))
if user>=3 or user<0:
    print("invalid .no such items")
else:
    system=random.randint(0,2)
    print("system selected")
    print(system)
    if(user==system):
        print("its a draw.\n")
    elif system==0 and user==2:
        print("you lose.\n")
    elif system==2 and user==0:
        print("you wins.\n")
    elif user > system:
        print("you wins.\n")
    elif system > user:
        print(" you lose.\n")

print("thanks to play.\n")


