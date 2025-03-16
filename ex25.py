# WE ARE SEEN A LIST AND TUPLES NEXT IS SETS..WE ARE REPRESENT A SETS IN {}..
set1={True,'deepak',1,1.5,1}# DUPLICATES ARE NNOT ALLOWED IN SETS CAN WRITE ONLY ONE NUMBER..
print(set1)# WE CAN RUN THE MULTIPLE DATA IN THE SETS..
set2={1,-2,-0.3,8,10,54,66}
print(set2)# we can seen a out that we can not get what we print in sets it mit be diffrent..
#print(set2[0])# WE CAN NOT PERFORME A INDEXING IN SETS BECAUSE OF NOT IN SAME CONDITION..
set3={}
print(type(set3))# AN EMPTY SET IT IS IN DICTNARY FORMATE
# WE CAN WRITE A DICT INTO THE SET BY USING..
set4=set()
print(type(set4))# WE GOT AN EMPTY SET BY USING ANOTHER WAY IS SET()..
#a=set4[0]=34
#print(a)# WE CAN'T DO THE ASSGINMENT OPERATION IN SET OPERATION..
# WE CAN DO ADDING AND REMOVING AN ELEMENT FROM THE SETS.
set2.add(34)
print(set2)# WE CAN ADDING VALUE TO THE SET 34 TO SET2..
print(len(set2))# we can find the length of a sets
set2.remove(1)
print(set2)# WE CAN REMOVE THE 1 FROM A SETS..
#ANOTHER TO REMOVE AN ELEMENT IS DISCARD.
set2.discard(-2)
print(set2)
# we can clear the sets by using a clear..
set2.clear()
print(set2)# its all the elements are clear..
# by using a pop function it can remove a randome element from a sets..
#set2.pop()
#print(set2)
set2.add((1,2,3,4))
print(set2)
