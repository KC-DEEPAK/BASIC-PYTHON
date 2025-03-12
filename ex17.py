# we are checking a leap year are not we have some condition..

year=int(input("enter the year you want to search.\n"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("its a leap year.\n")
        else:
            print("leap year.\n")

    else:
        print(" leap year.\n")
else:
    print("not a leap year.\n")
