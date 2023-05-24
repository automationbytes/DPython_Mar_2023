class employee:

    #class variable
    max_age = 60

    def __init__(self,name,age):
        #instance Variables
        self.name = name
        self.age = age

    @classmethod
    def set_retireage(cls,max_age):
        cls.max_age = max_age

    #static method

    @staticmethod
    def printtotal():
        print("Max age:", employee.max_age)

emp1 = employee("Tom",25)
emp2 = employee("Tim",23)
emp3 = employee("Jack",24)

em.set_retireage(55)

print(emp1.name,"is",emp1.age,"years old")
print(emp2.name,"is",emp2.age,"years old")
print(emp3.name,"is",emp3.age,"years old")


emp1.printtotal()
