class halloclass:
    def newfun(self,name):
        self.name=name
        print(name)

class subclass(halloclass):
    def subclassfunc(self,name):
        print(name)
        print(self.name)

obj = subclass()
obj.newfun("Nikhil")

obj.subclassfunc("hello")
