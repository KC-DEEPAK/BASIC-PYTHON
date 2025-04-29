
# DICTIONARY
phon_num={
    'raju':4354,
    'teju':9756,
    'manju':7656
}
phon_num['teju']=9867# inserting an elements to the dic
print(phon_num)# we can access the phon numbers only by printing a key name
phon_num.pop('raju')
print(phon_num)# deleting the elements .
# we can also add the tuples and lists and sets to the dic
phon_num['manju']=[3444444]
print(phon_num)
# we can also print the values and keys from dict
print(phon_num.keys())
print(phon_num.values())
print(phon_num.items())
phon_num.clear()
print(phon_num)# dic is full clear

# its a problematic dictionary
marks_dic={
    'kc':93,
    'kj':80,
    'my':55,
    'ks':22
}
for student in marks_dic:
    marks=marks_dic[student]
    if marks > 90:
        print(f"{student} you got A+ grade.\n")
    elif marks> 80:
        print(f"{student} you got A grade.\n")
    elif marks > 70:
        print(f"{student} you got B+ grade.\n")
    elif marks > 60:
        print(f"{student} you got B grade.\n")
    elif marks > 51:
        print(f"{student} you got C grade.\n")
    elif marks > 41:
        print(f"{student} you got D grade.\n")
    elif marks < 40:
        print(f"{student} you are FAIL IN EXAM.\n")
    else:
        print("invalid syntax.\n")
