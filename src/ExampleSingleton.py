class ExampleSingleton():

    __uniqueInstance = None
    name = ""

    def __new__(cls,name):
        if ExampleSingleton.__uniqueInstance is None:
            ExampleSingleton.__uniqueInstance = object.__new__(cls)
        ExampleSingleton.name = name
        return ExampleSingleton.__uniqueInstance

    def hello(self):
        print("Hello",self.name)

if __name__ == "__main__":
    exampleSingleton = ExampleSingleton("Derek");
    exampleSingleton.hello()
    exampleSingleton = ExampleSingleton("Matt");
    exampleSingleton.hello()
