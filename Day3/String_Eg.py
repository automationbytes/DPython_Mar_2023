'''
String - Datatype 
Anything which is surrounded by single/double quotes
'''

a = "Hello"
b = 'Hello'
print(a)
print(type(a))
print(b)
print(type(b))


multi = '''Python is one of the strongest data analytics programming language.
We can also use python as general purpose language to build application in desktop, Web, Database etc.
It supports multiple OS.'''

print(multi)
print(type(multi))

#Length of a string
a = "PYTHON"
print(len(a))

#Indexing- Char at that specified index
print(a[4])

#Negative Indexing- Char at that specified index
b = "Your booking id is:4578"
print(b[-4])

#Slicing - Cutting down the string
print(b[0:4])

#Negative slicing
print(b[-4:])

c = 'Your {Booking} id is :4578'
print(c[6:13])

#Strip - Cutting down the white spaces

d = "   Hello   World    "
print(d.strip())
print(d.rstrip()) #cut down the spaces on right side
print(d.lstrip()) #cut down the spaces on left side 

e = "helloWorld"
print(e.lower())
print(e.upper())

f = "Graß"
print(f.lower())
print(f.casefold())

g = 'python is one of the strongest data analytics programming language'
print(g.capitalize())
print(g.title())

h = 'Python Is One Of The Strongest Data Analytics Programming Language'
print(h.swapcase())


words = h.split(" ")
print(words)

c = 'Your citi bank {Booking} id is :4578'
#sp = c.split('{')
print(c.split('{')[1].split('}')[0])

#replace
print(c.replace("citi","sbi"))

#concat
a = "mango"
b = 10
print(a+str(b))
print(type(b))
print(a+format(b))


txt = "My friend name is {name} and he is {age} years old".format(name="Tom",age=5)
print(txt)


txt = "My friend name is {0} and he is {1} years old".format("Tom",5)
print(txt)



txt = "My friend name is {} and he is {} years old".format("Tom",5)
print(txt)

prdprice = "Price of the apple is {price:.3f} rupees!"
print(prdprice.format(price=89))

a = "Your total score is {:%}"
print(a.format(0.75))


a = "Your total score is {:.0%}"
print(a.format(0.75))


c = 'Your citi bank {Booking} id is :4578'
startindex = c.find("{")+1
endindex = c.find("}")
print(c[startindex:endindex])

print(c.split(":")[1])