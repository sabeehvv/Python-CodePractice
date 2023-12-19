class Bankuser:
    def __init__(self, name, AcNo):
        self._name = name
        self._AcNo = AcNo

    
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, value):
        self._name = value


    @property
    def AcNo(self):
            return self._AcNo


    @AcNo.setter
    def AcNo(self, value):
            self._AcNo = value


obj = Bankuser("user",39476864)

obj.name = "sabeeh"
obj.AcNo = 34567898765

print(obj.name)
print(obj.AcNo)