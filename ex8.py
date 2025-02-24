#operaters are in python
#arthimatic operator (+,-,*,/,%)
print(2**4)#by using a power operator
print(5+2*(3-1)+10/5)#pamdas
print(int(10*3+10/2))#in this we have 1st division and multiplication have a same presidance,that why we are LEFT TO RIGHT
print(int((10+3)+3*4))#IN THIS 1ST presidence is to brakets are more prefirance than multiplication and division
print(6/2)#its a normal division where we can get float.0 somthing
print(6//2)#this is called as flow division where we cant get float value
#calucalating body mass index BMI
w=float(input("enter the wight in kg \n"))
h=float(input("enter the hight in miter \n"))
formula=w/(h*h)
print(formula)