'''
Dict - Use key and value pair
ordered -3.7
changeable
duplicates keys not allowed

{}
'''


mydict = {
"name": "Tom",
"fruit": "Mango",
"vegetable": "Potato",
"language":"Python"

}
print(mydict)

print(mydict["fruit"])
print(mydict.get("fruit"))

print(len(mydict))

#print only keys
print(mydict.keys())

#print only values
print(mydict.values())

#print in pairs
print(mydict)

print("*********")
print(mydict.items())



stud1 = {
    "name" : "Tom",
    "rollnum" : "789"
}
stud2 = {
    "name" : "Jerry",
    "rollnum" : "123"
}

mystud = {
    "stud1":stud1,
    "stud2":stud2
}
print(mystud["stud2"]["rollnum"])


mydict = {
"name": "Tom",
"fruit": "Mango",
"vegetable": "Potato",
"language":"Python",
"fruit": "Banana",

}
print(mydict)
print(type(mydict.keys()))


txt = "Hello World"
print(txt.find("e"))

#loops
#iterating wit keys
for k in mydict.keys():
    print(k)


#iterating wit values
for k in mydict.values():
    print(k)

for k in mydict.keys():
    print(mydict[k])

for k,v in mydict.items():
    print(k,"--",v)
