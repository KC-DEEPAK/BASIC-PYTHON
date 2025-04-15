# function is a repetation of the block of code by calling a function.
# syntax of function is .
# def function name (parameter):we can define the variable in the parameter.
    # function body
        #return given expression.
# example
# calling a function
# function name ()
def fun():
    print("Deepak.KC\n")
fun()# this is called as a calling a function.
# we are trying a example of we passing the varible in function.
def add_two_num(num1,num2):
    num3=num1+num2
    print(num3)
add_two_num(1, 2)# this the way of passing a value in function.
def mul_two_val(a,b):
    c=a*b
    print(c)
mul_two_val(2,4)# we get 8 answer.
# function definition
def find_square(num):
    result = num * num
    return result# with the return we can return the end result.
# function call
square = find_square(3)

print('Square:', square)
# calucating a squar and cube by using a function.
def squar_and_cube(number):
    squar=number**2
    cube=number**3
    print('square is =',squar)
    print('cube is =',cube)
squar_and_cube(3)
squar_and_cube(4)
squar_and_cube(6)
# returing the value .
def add_number(a,b):
    return a+b
result=add_number(3,5)
print("result is ",result)


