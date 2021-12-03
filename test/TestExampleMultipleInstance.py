from src.ExampleMultipleInstance import ExampleMultipleInstance
import unittest

class TestExampleMutlipleInstance(unittest.TestCase):

    def testExampleMultipleInstance(self):
        firstInstance = TestExampleMutlipleInstance()
        secondInstance = TestExampleMutlipleInstance()
        self.assertIsNot(firstInstance,secondInstance)

if __name__ == "__main__":
    unittest.main()
