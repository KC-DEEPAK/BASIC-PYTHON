# while loop which is the loop is similar to the for loop in this we can declare the how many time the loop will be
#executed
count=1
while count<=5:
    print(count)
    count+=1
    if(count==5):
        break
else:
    print("dhanush")# in this we are known that when we use the break statment else block is not exsisties.

# in this we can seen that while else block with out a break:
count=1
while count<=5:
    print(count)
    count+=1
else:
    print("raju")
# while loop always ture when we give somthing to break.
count=0
while True:
    count+=1
    print(count)
    if(count==7):
        break
else:
    print("else block")
print("true")# in this we are not given a condition to the while loop insted of the condition loop always true untill the break
count=0
number=int(input("enter the values.\n"))
while number!=0:
    count+=1
    count=count+number
print(count)
