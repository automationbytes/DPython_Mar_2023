class employee:

    #class variable
    total_emp = 0

    def __init__(self,name,age):
        #instance Variables
        self.name = name
        self.age = age
        employee.total_emp += 1 

    #static method
    @classmethod
    def toprint(cls):
        total_emp = 0
        print(total_emp)

    @staticmethod
    def printtotal():
        print("Total Employee:", employee.total_emp)


emp1 = employee("Tom",25)
emp1.toprint()
emp2 = employee("Tim",23)

emp2.toprint()
emp3 = employee("Jack",24)
emp3.toprint()

emp4 = employee("Jim",24)


emp4.toprint()


print(emp1.name,"is",emp1.age,"years old")
print(emp2.name,"is",emp2.age,"years old")
print(emp3.name,"is",emp3.age,"years old")


employee.printtotal()