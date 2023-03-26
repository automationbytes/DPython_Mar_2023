'''
Operators - Used to perform certain operations on variables and values

1) Arthimetic Operators
2) Assignment Operators
3) Comparison  Operators
4) Logical Operators
5) Identity Operators
6) Membership Operators
7) Bitwise Operators

'''

#Arthimetic Operators - to perform basic arthimetic equations

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b) #float
print(a//b) #floor division (quotient alone with out decimal point)
print(a%b) #mod - remainder
print(a**b) #exponential - 


#Assignment Operator -  Assigning values back to the variables
x = 5

x += 3 # x = x+3

print(x)


#Comparison Operators

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical Operators
'''

and
---
true and true = true
true and false = false
false and true = false
false and false = false


or
--
true or true = true
true or false = true
false or true = true
false or false = false

not
---
true -> false
false - true
'''

a = 10
b = 5
c = 3
print("=======And======")
print(a<b and a>c)


print("=======OR======")
print(a<b or a>c)


print("=======NOT======")
print(not(a<b or a>c))

#Identity Operators - is and not is -> check both values belongs to same memory

x = ["Apple", "Banana"]
y = ["Apple", "Banana"]
z = y
print(x is y) # false - not belongs to same object 
print(y is z) # true - it belongs to same object
print(x == y) #juz check the value - true

#membership operator - to verify whether the values present or not
x = ["Apple", "Banana"]
print("Apple" in x)
print("Cherry" not in x)

y = "Naga"
print("y" in y)

x = 9 #   1001
y = 4 #   0100

print(x & y)
print(x | y) #1101
'''
1 and 1 = 1
1 and 0 = 0
0 and 1 = 0
0 and 0 = 0



'''
