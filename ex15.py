#  WE ARE NOW NESTED IF ELSE..we are taking a example
# condision when the booking a bus ticket.
hight=int(input("enter the hight in feet.\n"))
if(hight<=3):
    print("able to enter the bus.\n")
    age=int(input("enter the age.\n"))
    if(age<=5):
        print("pay only 250 rs.\n")
        print("wellcome.\n")
    else:
        print("pay 500 rs.\n")
else:
    print("not able to enter the bus.\n8")
    print("sorry.\n")
#elif condition..
num=int(input("enter the number.\n"))
if(num==1):
    print("one.\n")
elif(num==2):
    print("two.\n")
elif(num==3):
    print("three.\n")
