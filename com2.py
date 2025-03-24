# WE ARE CHECK WHEATHER A NUMBER IS NEGATIVE 0R POSITIVE OR ZERO.
num=float(input("enter the number you want to check.\n"))
if(num>0):
    print("its a positive number.\n")
elif(num==0):
    print("its a zero.\n")
else:
    print("its a negative number.\n")
# PRINT THE 1ST NATURAL NUMBERS USING A FOR LOOP.
n=11;
for i in range(1,n):
    print(i)# FOR PRINTING A 1ST 10 NATURAL NUMBERS.
# PRINTING A EVEN NUMBERS BY USING A FOR LOOP.
m=int(input("enter the end of the loop"))
for i in range(m):
    if(i%2==0):
        print(i)
# calucating the sum of odd number with in a given range.
y=int(input("enter the value of y.\n"))
sum=0
for i in range(y):
    if(i%2!=0):
        sum=sum+i
print("the sum of odd number is=",sum)
# PRINT A VALUES FROM LIST.
list=[1,3,-4,7]
for i in list:
    print("the values are =",i)
# COUNTING A NUMBER BY USING A FOR LOOP..
num1=input("enter the number to count.\n")
num1=str(num1)
#num1=['1','2','3','4','5']
count=0
for i in num1:
    count+=1
print("the total number of elements are =",count)
# this is by counting the number of elements are present in the string.