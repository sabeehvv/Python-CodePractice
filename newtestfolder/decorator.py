class testcalls:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def decorator(func):
        print("its outside innerfunction")
        func()
        print("Good Morning guys")

    print("inside class")
    
    @decorator
    def newtest():
        print("Decorators how is it working")
from datetime import datetime


def testtime(func):
    func()
    print(f'{"_"*30}')

def sample():
    print("Test f function")

output = testtime(sample)

print(output)


