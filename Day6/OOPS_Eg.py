'''
Student
    #attributes
    name
    mobile

    #methods
    study
    write

'''

class student:
    name = "Tom"
    age = 10

    def toStudy(self):
        print(self.name, "study method")

    def toWrite(self):
        print(self.name, "write method")

s = student()
s.toStudy()

class stud:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toStudy(self):
        print(self.name, "study method")

    def toWrite(self):
        print(self.name, "write method")

s1 = stud("Tom",5)
s2 = stud("Jack",15)
s3 = stud()

s1.toStudy()
s2.toStudy()
s3.toStudy()

