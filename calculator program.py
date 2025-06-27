# This project name is calculator project.
import os
def addition (a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
#creating a dictonary in to what operator perform what
opeartion_dict={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}

def calculator():
    num1=int(input("enter the value of num1 \n"))# taking a 1st input as num1
    for symbole in opeartion_dict:# we are using
        print(symbole)
    continue_flage=True
    while continue_flage:
        op_symbole=input("please select the operator =")
        num2=int(input("enter the value of num2 \n"))
        caculator_function=opeartion_dict[op_symbole]
        output=caculator_function(num1,num2)
        print(f"{num1} {op_symbole} {num2}={output}")# this is for giving a
        should_continue=input(f"enter the 'y' to continue the caculation with {output} or enter 'x' to start a new calculation 'n' to exit").lower()
        if should_continue=='y':
            num1=output
            # we are staring the fresh calculation
        elif should_continue=='x':
            continue_flage=False
            os.system('cls')
            calculator()
        else:
            continue_flage=False
            print("Bay")
calculator()












