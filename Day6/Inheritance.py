class Google:

    def loginPage(self):
        print("Login page of Google")

    def homePage(self):
        print("Home page of Google")


class Youtube(Google):

    def toPlay(self):
        print("Play Videos")

y = Youtube()
y.toPlay()
y.loginPage()

