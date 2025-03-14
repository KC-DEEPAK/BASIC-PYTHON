# CONCEPT OF TUPLE . IT IS SIMILAR TO LIST.TUPLE INDICATES BY ()
tuple1=(1,2,3)
print(type(tuple1))# THE DIFFRENCE IS () WITH COMMA AS TO BE PUT .
tuple2=(1)
print(type(tuple2))# AS IN TUPLE2 DONOT HAVE A COMMA AND IT IS A NOT A TUPLE AND IT IS TUPLE
tuple3=(True,'deepak',6,4.5)
print(tuple3)# WE CAN ALSO PEROFRAM ALL OPERATION IN TUPLE.
print(tuple3[1])
print(tuple3[-2])# WE CAN DO INDEXING IN A TUPLE
# IN TUPLE WE CANT INSERT AND DELETING THE VALUE FROM TUPLE DRABACK
#EXAMPLE.
#a=tuple3[0]=5
#print(a)# WE GOT AN ERROR OF TUPLE DOSENT SUPPORT A ASSGINMENT OPERATION
#b=tuple3.remove(6)
#print(b)# WE CANT DO DELEET OPERATIN ON TUPLE.
print(tuple3[1:3])# WE CAN DO SLISSING IN TUPLE
# WE DO NESTED OF TUPLE IN TUPLE.
#EXAMPLE
tuple5=(3,'deepak',True,3,3)
tuple4=(tuple1,tuple5)
print(tuple4)# WE CAN NESTED A TUPLES OR ADDING A TUPLE
print(tuple4[1])# in this we can acssess the reqired tuple which we reqired.
tuple6=(tuple3 + tuple5)
print(tuple6)# WE CAN CONCADINATION OF TWO TUPLE.
print(tuple5.index(3))# WE GOT A INDEX OF 3 IS OTH INDEX WE HAVE 3.
print(tuple5.count(3))
print(max(tuple1))
print(min(tuple1))# WE CAN DO MAX AND MIN OPERATION ON TUPLE.
print('THANKS')
