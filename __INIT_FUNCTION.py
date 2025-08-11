# INIT FUNCTION WE CAN SEE HOW WE CAN REPRESTING A FUNCTION
class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.instructor_address=address
        # we  can set a default value
        self.followers=0


instructor_1=Instructor("deepak","ckm")
print(instructor_1.name)
print(instructor_1.followers)

instructor_2=Instructor("puni","kyathanabeedu")
print(instructor_2.name)

instructor_3=Instructor("vishnu","kadur")
print(instructor_3.name)

instructor_4=Instructor("karan","mandya")
print(instructor_4.name)

class Employee:
    def __init__(self,ssn,name):
        self.number=ssn
        self.emp_name=name



employee_1=Employee("001","deepu")
print(employee_1.number)
employee_2=Employee("002","lohi")
print(employee_2.number)