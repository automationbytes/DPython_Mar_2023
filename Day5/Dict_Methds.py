
mydict = {
"name": "Tom",
"fruit": "Mango",
"vegetable": "Potato",
"language":"Python",
"fruit": "Banana",
"Veggies":"Potato"
}
print(mydict)

#adding items
mydict["color"] = "Blue"
print(mydict)

#update
mydict.update({"color":"Red"})
print(mydict)

#update
mydict.update({"Laptop":"Dell"})
print(mydict)


#Set default - if we hav key- it will nt update, else it iwll add
mydict.setdefault("Laptop","Hp")
print(mydict)

mydict.setdefault("Cricketer","Virat")
print(mydict)


mydict.setdefault("Cricketer","Dhoni")
print(mydict)

#pop - remove specified key 
mydict.pop("color")
print(mydict)

#popitem - it wil remove the last valye
mydict.popitem()
print(mydict)

#copy
newdict = mydict.copy()
print(newdict)

#clear
newdict.clear()
print(newdict)

del(newdict)
#print(newdict)


for k,v in mydict.items():
    if v == "Potato":
        print(k)