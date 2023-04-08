'''
Functions(Methods)
Set of lines which will be executed when its being called
Reusability


def functionname(parameters):
    return statement


'''

def sumOfTwoNumbers(a,b):
    return (a+b)

c = sumOfTwoNumbers(b=5,a=3) + 10
print(c)

add = lambda a,b : a+b
print(add(10,6))

def countrylist(country = "India"):
    return "Selected value is"+country

print(countrylist())

print(countrylist("Pak"))

