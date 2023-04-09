class Google:

    def __init__(self,name,location):
        self.name = name
        self.location = location

    def toPrint(self):
        print("Name:", self.name)
        print("Location:",self.location)

class Youtube(Google):

    def __init__(self, name, location, subscribtions):
        super().__init__(name, location)
        self.subscribtions = subscribtions

    def toPrintSubscription(self):
        print("subscribtions:",self.subscribtions)

myobj = Youtube("DevopsUniv","India",15000)
myobj.toPrint()
myobj.toPrintSubscription()
