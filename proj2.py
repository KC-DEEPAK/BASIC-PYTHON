 # PASSWORD GENRATORE BY USING A PYTHON.
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v''w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
symboles=['!','@','#','$','%','&','*','(',')','+','=']
print("wellcome to password generator.\n")
n_letters=int(input("enter the input how many letters you required.\n"))
n_numbers=int(input("enter the input how many numbers you required.\n"))
n_symboles=int(input("enter the number of symboles required.\n"))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    password_list+=num
for i in range(1,n_symboles+1):
    sym=random.choice(symboles)
    password_list+=sym
print(password_list)
random.shuffle(password_list)
password=''
for j in password_list:
     password+=j
print(password)