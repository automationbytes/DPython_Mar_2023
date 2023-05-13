import unittest

def setUpModule():
    print("Setup Module")

def tearDownModule():
    print("TearDown Module")

class Sampletest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")
    # def setUp(self):
    #     print("Setup test")

    # def tearDown(self):
    #     print("Teardown test")

    def test3(self):
        print("Test 3")
        
    def test1(self):
        print("Test 1")

    def test2(self):
        print("Test 2")


if __name__ == "__main__":
    unittest.main()
