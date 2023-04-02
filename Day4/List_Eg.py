'''
List is very similar to Array in other language
List is mutable(Modifiable)
Ordered - Insertion Order
List allows duplicates
List can be accessed wit index values
List can contain homo n hetro data (Same and diff data types)
[] - 
'''

fruits = ["Apple","Mango","Banana","Stawberry","Banana"]
print(fruits)

#length
print(len(fruits))

#indexing - it starts from first value and starts wit 0
print(fruits[0])
#negative indexing (from last value)
print(fruits[-1])

#Slicing - Cutting down the list into smaller pieces
print(fruits[1:4])

#Negative slicing
print(fruits[-4:-1])

print(fruits[-5:])
print(fruits[2:])

print(fruits[:-2])

#reverse a list
print(fruits[::-1])


fruits = ["Apple",5,"Mango","Banana",3.54,"Stawberry","Banana"]

for f in fruits:
    print(f)

print("Normal for loop")
for i in range(0,len(fruits),1):
    print(fruits[i])
