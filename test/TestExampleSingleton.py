from src.ExampleSingleton import ExampleSingleton
import unittest

class TestExampleSingleton(unittest.TestCase):

    def testExampleSingleton(self):
        firstInstance = ExampleSingleton("Derek")
        secondInstance = ExampleSingleton("Matt")
        self.assertIs(firstInstance,secondInstance)

    def testExampleSingletonName(self):
        firstInstance = ExampleSingleton("Derek")
        secondInstance = ExampleSingleton("Matt")
        self.assertEqual("Matt",firstInstance.name)

if __name__ == "__main__":
    unittest.main()

