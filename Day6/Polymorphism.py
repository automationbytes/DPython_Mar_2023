class Google:

    def loginPage(self):
        print("Login page of Google")

    def homePage(self):
        print("Home page of Google")


class Youtube(Google):

    def homePage(self):
        print("Home page of Youtube")

    def toPlay(self):
        print("Play Videos")

y = Youtube()
y.toPlay()
y.loginPage()




class parent:

    def bride(self):
        print("Bride name is Jenny")

    def prop(self):
        print("4 BHK with some gold")


class child(parent):

    
    def bride(self):
        print("Bride name is Jessy")


c = child()
c.bride()
c.prop()