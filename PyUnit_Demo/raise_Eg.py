import unittest

def div(a,b):
    return a/b

class raiseTest(unittest.TestCase):
    def testRaise(self):
        self.assertRaises(ZeroDivisionError,div,1,10)

if __name__ == "__main__":
    unittest.main()