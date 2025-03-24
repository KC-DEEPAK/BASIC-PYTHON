# FOR LOOP IN PYTHON ..
names=['ram','nikhil','shiva','srujan','sanjay']
for name in names:
    print(name)# ITS WORKING WE ARE CREATED A VARIABLE NAME IS NAME WHEN THE CONDISION IS TRUE ITS PRINT STORED DATE NAME.
# WE CAN TRY WITH STRING ALSO..
games='car'
for game in games:
    print(game)# ITS WORK WHEN WE GIVEN A STRING..
# WE CAN TAKE A INTEGER PART ALSO..
number=[2,3,4,5,6,8,-3]
squares=[]
for i in number:
    square=i**2
#print(sq)# WE HAVE TO PRINT THIS IN A LIST.
    squares.append(square)
    print(squares)# IN THIS OPERATION WE ARE DONE THE HOW TO SQUARE THE LIST AND PRINT.
    if(i==4):
        print("even")
        break
else:
    print("sum of this numbers")# else is executed when the
