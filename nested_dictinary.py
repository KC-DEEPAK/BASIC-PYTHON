# nested_dictinary which we create a inside a dictinary another dictinary .
student_data={
    "ramu":{"marks":96,"age":13},
    "ram":{"marks":76,"age":22}
}
print(student_data)
# this is by creating a nested dict:
# next we can add the key and value to the dictinary.
student_data["ramu"]["roll_num"]=29
print(student_data["ramu"])
# this is how we can add the data to dict
# we can also do the delete operation we can use a del or pop.
del student_data["ramu"]["age"]
print(student_data["ramu"])
# we delete the value by del key word.
# now we are using a pop key it return the value which is deleted .
print(student_data["ram"].pop("marks"))
print(student_data["ram"])
# we deleted value by pop keyword.


