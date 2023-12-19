from abc import ABC, abstractmethod

class Calculator(ABC): 
    def __init__(self):
          pass
    

    @abstractmethod 
    def add (self):
           pass
    def sub(self):
          pass
    def mul(self):
          pass
    def div(self):
          pass
    
class functions(Calculator):
      
    def add(self,num1,num2):
        result = num1+num2
        print("Result is : ",result)

    def sub(self,num1,num2):
         result = num1-num2
         print("Result is : ",result)

    def mul(self,num1,num2):
        result = num1*num2
        print("Result is : ",result)

    def div(self,num1,num2):
         result = num1/num2
         print("Result is : ", result)

obj = functions()
num1 = int(input("Enter 2 numbers \n"))
num2 = int(input())
choice = int(input("Select your choice \n1 :Addition \n2 :Substraction \n3 :Multiplication \n4 :Devision \n =>"))

match choice:
    case 1:
          obj.add(num1,num2)
    case 2:
          obj.div(num1,num2)
    case 3:
          obj.mul(num1,num2)
    case 4:
          obj.sub(num1,num2)
    case default:
          print("Select correct number")