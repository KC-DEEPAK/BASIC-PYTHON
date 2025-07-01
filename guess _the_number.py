import random
import art_logo
from tabnanny import check

EASY_LEVEL_ATTEMPTES=10
HARD_LEVEL_ATTEMPTES=5
def set_dificulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTES
    else:
        return HARD_LEVEL_ATTEMPTES

def check_answer(guess_number,answer,attemptes):
    if guess_number<answer:
        print("your guess is too low" )
        return attemptes-1
    elif guess_number>answer:
        print("your guess is too high")
        return attemptes-1
    else:
        print(f"your guess is right answer was {answer}")

def game():
    print(art_logo.logo)
    print("let me think about the number between 0 to 50")
    answer=random.randint(1,50)
    level=input("choose the level dificulty..type 'easy'or'hard':")
    attemptes=set_dificulty(level)
    guess_number=0
    while guess_number!=answer:
        print(f"you have  {attemptes} attemptes remaing to guess the number ")
        # we are declere the funtion to checke the random guess and user guess are same
        guess_number=int(input("enter your guess"))
        attemptes=check_answer(guess_number,answer,attemptes)
        if attemptes==0:
            print("you are out of guess ...you lose")
            return
        elif guess_number!=answer:
            print("gusse again")
game()