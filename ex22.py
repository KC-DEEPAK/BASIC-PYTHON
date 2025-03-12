# RANDOM MODULE WHICH ITS CAN SELECTED ANY RANDOM ELEMENT IN THE PROGRAM
import random
a=random.randint(1,3)
print(a)#in the randint function which is selecte the numbers between the 1 and 3.
a=random.randrange(1,5)# its include upto the 4 it will be select
print(a)
#when we reqired a floating point..
a=random.random()
print(a)
a=random.uniform(1,4)
print(a)
l=[22,33,43,56,6,7,8,4]
b=random.choice(l)
print(b)
# we can shuffal the list by random
random.shuffle(l)
print(l)# we have a complete list we not storing a data in variable..

# RANDOM PROGRAM .HEAD(1) OR TAIL(0)
a=random.randint(0,1)
print(a)
if(a==0):
    print("0 indicates a tail.\n")
else:
    print("1 indicates a head .\n")

