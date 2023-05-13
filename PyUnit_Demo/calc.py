import unittest

class simpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4+4,9,"Both are equal")

if __name__ == "__main__":
    unittest.main()
