fruits = ["Apple","Mango","Banana","Stawberry","Banana"]
vegetables = ["Tomato","Onion","Carrot","Potato","Carrot"]

#append - add a single value to the list, it will add the values at the end of the list
fruits.append("Orange")
print(fruits)

# fruits.append(vegetables)
# print(fruits)

#extend- to combine two list

fruits.extend(vegetables)
print(fruits)


#insert - inserting values in speciifed index
fruits.insert(2,"Blueberry")
print(fruits)


#remove - removes the first matching element
fruits.remove("Banana")
print(fruits)

#Pop - used to remove last value
fruits.pop()
print(fruits)

#pop with index
fruits.pop(3)
print(fruits)

newfruits = fruits.copy()
print(newfruits)

#clear - will empty our list, but variable will be on memory
newfruits.clear()
print(newfruits)
newfruits.append("Hello")
print(newfruits)
#del - variable also wilbe removed from memory
del(newfruits)

#count
fruits.extend(fruits)
print(fruits)
print(fruits.count("Banana"))

fr = ['Apple', 'Banana', 'Banana', 'Orange',['Blueberry', 'Banana', 'Orange',"Orange"]]
print(fr.count("Orange"))

vegetables = ["Tomato","Onion","Carrot","Potato","Carrot"]
print(vegetables.index("Carrot"))


#sort
vegetables.sort()
print(vegetables)

#reverse - descending order
vegetables.sort(reverse= True)
print(vegetables)

# fruits = ["Apple",5,"Mango","Banana",3.54,"Stawberry","Banana"]
# fruits.sort()
# print(fruits)

num = [5,8,9,1,4,3]
num.sort()
print(num)

alphabets = ["Zebra","Ball","Dog","Elephant","Parrot"]
alphabets.sort(reverse=True)
print(alphabets)

alphabets = ["Zebra","Ball","Dog","Elephant","Parrot"]
alphabets.reverse()
print(alphabets)


