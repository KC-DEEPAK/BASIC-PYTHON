# IN PYTHON WE HAVE A FUNCTION AND WE PASS SOME ARGUMENT IN FUNCTION.
          # EXAMPLE
def greet(name):# this are parameters where the indicated the storage a value or variable.
    print(f"hai {name}.")
    print("are you from cse.")
greet("raju")# this are all arguments storing a value to variable.
greet("hemanth")
def add(x,y):
    z=x+y
    print(f"sum of two numbers is {z}")
add(2,3)
add(45,77)


  # TYPES OF ARGUMENT .
# 1) POSITIONAL ARGUMENT.
def greet(name,department):
    print(f"hai {name} how are you")
    print(f"are you from {department} department")
greet('deepak','cs')
# THIS IS CALLED AS POSITIONAL ARGUMENT.

  # 2)default argument .
def greet(name,subject,department="me"):
    print(f"hai {name} ")
    print(f"are you taking {subject} subject")
    print(f"in {department} department ")
greet("deepak","dbms","cs")# this is called as default condition where the argument is overwrite
# by calling the function.


   #3) arbitary argument.
def add(*numbers):# *args the condition
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c} ")
add(2,3,4,5,6)
add(66,88,88,77,55)# this is called as arbitary argument and this is use to we can pass n numbers of argument,


 # 3) kwargs argument.
def info_stu(*args,**kwargs):# this is called as key warded argument and it only accepect the keyword argument
    for i,j in kwargs.items():
        print(i,j)
    print(args)
info_stu(6,7,8,name='deepak',age=12,id=2332)
info_stu(1,2,3,4,name='vinay',age=34)# also we can add the *args to the **kwargs and we follow the rules 1st we should write the
# args after we acn call the **kwargs


# assingnment problem we should multiply the numbers by using a argument.
def multiple(*multi):
    c=1
    for i in multi:
        c=c*i
    print(f"the total of multiplication is {c}")
multiple(2,3,-6,8)
multiple(2,5,8,9,0,6)












