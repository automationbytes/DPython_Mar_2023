'''
Tuple - Ordered
And unchangeable (Unmutable)
Duplicates are allowed
Can hav hetro and homo data types

() - Without brackets
'''

fruits = "Apple","Mango","Banana","Grapes","Apple"
print(fruits)
print(type(fruits))

#indexing
print(fruits[1])

#negative indexing
print(fruits[-1])

#Slicing
print(fruits[1:3])

#Negative Slicing
print(fruits[-3:-1])

#update/add/remove
newlist = list(fruits)
newlist.append("Stawberry")
fruits = tuple(newlist)
print(fruits)

#unpacking
fruits = "Apple","Mango","Banana","papayya","Grapes"
(red,*yellow,black) = fruits
print(yellow)

#for loop
for f in fruits:
    print(f)

for i in range(len(fruits)):#start 0 and step 1
    print(i,fruits[i])


stud = ("Tom","Jack","Hendry")
(r101,r105,r109) = stud
print(type(r109))


#count
fruits = "Apple","Mango","Banana","Papayya","Grapes","Apple"
print(fruits.count("Apple"))

#index
print(fruits.index("Mango"))

#sort
newfruits = list(fruits)
newfruits.sort()
fruits = tuple(newfruits)
print(fruits)
