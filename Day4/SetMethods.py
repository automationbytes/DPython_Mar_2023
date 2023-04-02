#add - it will simply insert value (any random position)
vegetables = {"Tomato","Onion","Carrot","Potato","Carrot"}
vegetables.add("Beetroot")
print(vegetables)

#update - add two sets
vegetables = {"Tomato","Onion","Carrot","Potato","Carrot"}
fruits= {"Apple","Banana","Stawberry"}

vegetables.update(fruits)
print(vegetables)

#remove
vegetables.remove("Apple")
print(vegetables)

#pop
vegetables.pop()
print(vegetables)

#discard
vegetables.discard("Tom")
print(vegetables)

newveg = vegetables.copy()
print(newveg)

newveg.clear()
print(newveg)

del newveg

employee = {"Ram","Tom","Tim"}
student = {"Ram","Sita","Jerry"}
print(employee.intersection(student))

print(employee.symmetric_difference(student))

print(employee.union(student))


print(employee.difference(student))
print(employee)