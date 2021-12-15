#swap key as a value and value as a key
dict1={'a':1,'b':2,'c':3,'d':4}
new_dict=dict([(value,key) for key,value in dict1.items()])
print(new_dict)

#swap key as value-multiple same values in one unique key
dict2={'a':1,'b':2,'c':3,'d':4,'e':2,'f':4,'g':4}
new={ }
for key,value in dict2.items():
    if value in new:
        new[value].append(key)
    else:
        new[value]=[key]
print(new)