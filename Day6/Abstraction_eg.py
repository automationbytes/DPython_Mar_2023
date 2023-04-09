from abc import ABC


class parent(ABC):

    def bride(self):
        pass

    def prop(self):
        print("4 BHK with some gold")


class child(parent):    
    def bride(self):
        print("Bride name is Jessy")

c = parent()
c.bride()
