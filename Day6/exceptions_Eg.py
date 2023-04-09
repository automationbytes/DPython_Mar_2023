'''
try - test the block of code with errors/
except - block used to handle errors caused in try block
finally - irrespective of results. cleanup activities
else - no errors in try blck (optional)

'''

import traceback
try:
    num = 10
    print(10/0)

except:
    print("An exception occured")
    traceback.print_exc()

# finally:
#     print("Finally")

 
else:
    print("Else part")
   
print("Hello")




try:
    num = 10
    print(a)

except NameError:
    print("Variable is not defined")
    traceback.print_exc()

except ZeroDivisionError:
    print("Number divided by zero")
    traceback.print_exc()


#raise - for raising customized exception

age = 5
if age < 18:
    raise Exception("Sorry not eligible for voting")