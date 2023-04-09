class stud:

    schoolname = "Devops Univ"
    _course = "Python Protected"
    __year = "2023 private"

    #public
    def publicmethd(self):
        print("Public method")
    
    def _protectedmtd(self):
        print("Protected Methd")

    def __privatemethd(self):
        print("Private Methd")

class chstd(stud):
    def hello(self):
        pass
s = chstd()
s.publicmethd()