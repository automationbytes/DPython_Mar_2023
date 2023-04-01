i = 1
while i <= 10:
    print(i)
    i = i+1

#reverse a number
num = 1234
#4321
reversenum = 0

while num > 0:
    remainder = num % 10 #4 #3
    reversenum = reversenum * 10 + remainder #4*10 + 3 = 43
    num = num // 10 #123
print(reversenum)
print(type(reversenum))

num = 1234
rev = str(num)
print(rev[::-1])
print(type(rev))