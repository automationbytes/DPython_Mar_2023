a = 1
b = 5

if a > b:
    print("A is greater")
else:
    print("B is greater")

a = 1
b = 5
c = 8
if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
else:
    print("C is greater")

#Short Hand
if a < b : print("A")

a = 5
b = 3
print("A") if a < b else print("B")



a = 5
b = 5
print("A") if a < b else print("B") if a > b else print("==")


num = 25
if(num > 10):
    print("Num is above 10")

    if(num > 20):
        print("Num is above 20")
        if(num > 30):
            print("Num is above 30")
        
'''
Numbers - odd/even
Num - positive/negative
Student Marklist - add them
80 - A
60-79 -B
40-59 - C
Less than - F

'''

print("Enter 3 numebrs")
a,b,c = int(input()), input(), input()
print(a, "this is a value")
print(b, "this is b value")
print(c, "this is c value")
print(type(a))


a,b,c = 40,50,60
print(a, "this is a value")
print(b, "this is b value")
print(c, "this is c value")