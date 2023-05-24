'''
Set - Similar to list 

it is mutable (modifiable)
it will not maintain order
it will not allow duplicates
it will not allow indexing
{} 
we can store both homo and hetro datatype

'''

vegetables = {"Tomato","Onion","Carrot","Potato","Carrot"}
print(vegetables)

fruits = ["Apple","Mango","Banana","Stawberry","Banana"]
newfruits = set(fruits)
print(newfruits)


for n in newfruits:
    print(n)

for i in range(0,len(newfruits),1):
    print(newfruits[i])
