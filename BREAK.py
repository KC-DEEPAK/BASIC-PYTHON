# WE HAVE CONTOLE STATMENTS IN THE PYTHON ARE
#                    1)BREAK .IT IS A STOP OF THE LOOP EITHER A FOR OR WHILE LOOP.
#                    2)CONTINUE.IT IS CONTINUE THE LOOP UP TO WHERE WE WANT THE LOOP.
#                    3)PASS. THIS IS EITHER SKIP THE LOOP OR PASS.
#       EXAMPLE
list1=["hai","hello","bai"]
list2=["pavan","rahul","puni"]
for item in list1:
    for name in list2:
        print(item,name)
        if(item=="hai" and name=="pavan"):
            break # this is for where we can break the loop and out side the loop will executed on nearest for loop
    print("inside the loop")
print("out side the loop")


  # it is a another contole statment is continue .
count=1
while count<=9:
    print(count)
    count = count + 1
    if(count==5):
        continue
    print("hai")
print("out side the loop")# its a continue of the loop without stoping the loop which we given value onle thatcan be skip.
# let take a simple example .
for i in range(0,10):
    if(i==4):
        continue
    else:#  it skip the 4
        print(i)
print("outside the loop")
