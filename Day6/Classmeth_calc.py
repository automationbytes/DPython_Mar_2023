class Maths:

    @classmethod
    def add(cls,a,b):
        return a+b

    
    @classmethod
    def sub(cls,a,b):
        return a-b

print(Maths.add(5,6))

mat = Maths()
print(mat.add(5,6))
