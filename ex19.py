print("PIZA ORDER PROGRAM.\n")
bill=0
size=(input("enter the size of the piza.\n"))
if size=='S' or size=='s':
    print("its cost about 100 RS.\n")
    bill+=100
elif size=='M' or size=='m':
    print("its cost about 200 RS.\n")
    bill+=200
elif size=='L' or size=='l':
    print("its cost about 300 RS.\n")
    bill+=300
else:
    print("not avalible in the store.\n")
paparoni=input("do you want a paparoni(yes/no).\n")
if paparoni=='y' or paparoni=='Y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill += 50
else:
    print("paparoni is not avalible.\n")
print(f"your final bill is {bill}.\n")
chesse=input("do you want a  chesse.\n")
if chesse=='Y' or chesse=='y':
    if size=='S' or size=='s':
        bill+=40
    else:
        bill+=65
else:
    print("chesse is not avalible in the store")
print(f"total amount is {bill}.\n")
print("THANKS TO PERCHASE THE ITEMS.\n")


