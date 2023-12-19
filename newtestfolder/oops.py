class Model:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.newc=44

    def testfun(self):
        print(self.name,str(self.age))
    def first(self,num1,num2):
        result = num1+num2
        print(result)

class MOdelseccond(Model):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def first(self,num1,num2):
        result = num1*num2
        print(result)
        super().first(num1,num2)

objs = MOdelseccond("sabeeh",26)

objs.first(22,33)
objs.testfun()