'''
Variables - Identifier/Container to store some values

Starts with an alphabets/underscore
Shouldnt contain any special chars other than underscore
Shouldnt start numbers
Shouldnt hav any spaces in between

Variables are case sensitive

a = 10
A = 5


Datatype - type of the variable

numbers - int, float and complex
string - str
boolean - bool (true/false)

Sequence Types - list, tuple, range
Mapping Types - dict
Set Types - set, frozen set
None Type - NoneType
Binary Types - bytes, bytearray, memoryview


'''

a = 5
A = 10
print(a)
print(A)

#type - specify the data type

#int - whole numbers (Numbers without decimal points)
print(type(a))

#float - numbers with decimal point
b = 3.14
print(b)
print(type(b))

#complex - it includes real and imaginary part
c = 5+2j
print(type(c))

#str - storing text
d = "Hello World"
print(type(d))

#Sequence Types
#list
e = ["apple","ball","cat"]
print(type(e))

#tuple
f = ("apple","ball","cat")
print(type(f))

#range
g = range(10)
print(g)
print(type(g))


#set- 

f = {"apple","ball","cat"}
print(type(f))

#frozenset -

f = frozenset({"apple","ball","cat"})
print(type(f))


x = None
print(type(x))

y = b"Hello World"
print(y)
print(type(y))

z = bytearray(2)
print(z)
print(type(z))

q = memoryview(bytes(2))
print(q)
print(type(q))

