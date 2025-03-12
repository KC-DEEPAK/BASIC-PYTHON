# multiple if statment and elif by using this write an example..

age=int(input("enter the number.\n"))
if(age<=10):
    print("pay 200.\n")
    if(age<15):
        print("pay 240.\n")
        if(age<=18):
            print("pay 500.\n")
else:
    print("not able to pay age limit.\n")
    #in this we are under stand that if is check every condition..
# BY USEING A ELIF STATMENT HOW ITS WORK. BY EXAMPLE WE CAN SHOE IN THE BELOW.
entry=int(input("enter the ages to enter the company.\n"))
if(entry<=10):
    print("pay only 300 RS.\n")
elif(entry<15):
    print("pay only 500 RS.\n")
else:
    print("not able to enter the company")



