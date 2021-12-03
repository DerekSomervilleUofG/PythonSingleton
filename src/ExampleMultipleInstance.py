class ExampleMultipleInstance():

    name = ""

    def __init__(self,name):
        self.name = name


    def hello(self):
        print("Hello",self.name)

if __name__ == "__main__":
    exampleMultipleInstance = ExampleMultipleInstance("Derek");
    exampleMultipleInstance.hello()
