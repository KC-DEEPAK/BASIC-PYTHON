# LISTS this are the storing a data in a list manner by seprating by a commaes..

numbers=[1,-5,7,9,4]
print(numbers)#this is for integer part..
print(type(numbers))
names=["deepak,vijay,naveen,teju,parjwal"]
print(names)
print(type(names))
# WE CN REPRESENT A LIST IN A SQUER BARCKETS..[]
mix_list=[True,'deepak',1,10.55]
print(mix_list)# we can also show that the python we can executing a mixed list
# IN THE LIST WE CAN FIND THE LENGTH OF AN LIST BY USING LEN FUNCTION..
name=['rahul','kantha','vishnu','kushal','dhanvin']
print(len(name))
print(name[3])
# WE CAN DO THE Slicing in python..
class_usn=[1,2,3,4,5,6,7,8,45,87]
print(class_usn[0:10])
# WE ALSO HAVE EXTENDED SLICING..THIS ARE EXTANED BY GIVEN NUMBERS..
print(class_usn[0:4:2])
# WE ALSO DO OPERATION OF SORTING IN THE LIST
values=[10,-1,5,8,3,5,-3,-6]
values.sort()
print(values)
# we can do reverse
values.reverse()
print(values)
# we can do add to a list by using a insert,append,and want to insert a more thane one use a extend key.
values.append(34)
print(values)
values.insert(4,56)#we have to mention a position we going to insert a value.
print(values)
values.extend([9,45,22,58,58,58])
print(values)
values[1]=-2
print(values)# this is replacing a element by another..
values[1:5]=[55,77,88,66,45]
print(values)
# BY DELETING WE HAVE A TWO TYPES ARE REMOVE AND POP() OPERATION IN LIST.
values.remove(77)
print(values)#when we given the input and that element will remove in the list.
#ANOTHER WAY:
print(values.pop(1))
print(values)# its remove the index which element present at index 1 we can print which element is removed.
# COUNT METHOD
print(values.count(58))# yes we can count the apperence of numbers:




