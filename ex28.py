# NEXT IS RANGE FUNCTION BY USING A FOR LOOP.
#a=range(0,100,2)
#  SYNTAX IS range(start,end ,incremented by n)
total=0
for i in range(1,11):
    total+=i
print("the sum of 1st 10 numbers is=",total)

# CODING TASK IS THE SUM OF EVEN NUMBERS FROM 1 T0 100 BY USING A RANGE FUNCTION.

total=0
#for j in range(0,101,2):# ONE WAY OF SUM TO EVEN NUMBERS
for j in range(0,101): #AND ANOTHER WAY IS BY USING A CONDITION OF EVEN.
    if (j%2==0):
        total+=j
print("the sum of even number form 1 to 100 is =",total)

# fizz buzz job interview question.
#question is we have to print a number 1 to 100 in this which is divisible by 3 we have to call fizz and
# when it is divisible by 5 it should be print a buzz and both 3 and 5 print a fizzbuzz.
for k in range(1,101,1):
    if(k%3==0):
        print("fizz")
    elif(k%5==0):
        print("buzz")
    elif(k%3==0) and (k%5==0):
         print("fizzbuzz")
    else:
        print(k)