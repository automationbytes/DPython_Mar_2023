import unittest

class simpleTest(unittest.TestCase):

    @unittest.skip("Skip Test")
    def test1(self):
        print("test1")
    @unittest.skipIf(1==1,"Skip if will execute condition is false")
    def test2(self):
        print("test2")

    @unittest.skipUnless(1==1,"Skip unless will execute condition is true")
    def test3(self):
        print("test3")

    @unittest.expectedFailure
    def test4(self):
        print("test4")
        self.assertTrue(False)



if __name__ == "__main__":
    unittest.main()

