class mathematics:
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2

    def addition(self):
        # self.num1=num1
        # self.num2=num2
        result = num1+num2
        return result

    def subtraction(self):
        # self.num1 = num1
        # self.num2 = num2
        result = num1-num2
        return result

    def multiplication(self):
        # self.num1 = num1
        # self.num2 = num2
        result = num1*num2
        return result
        
    def division(self):
        # self.num1 = num1
        # self.num2 = num2
        result = num1/num2
        return result


def errormessage():
    return "Enter correct number"

num1 = int(input("Enter 2 numbers \n"))
num2 = int(input())
print("Select your choice \n1 :Addition \n2 :Substraction \n3 :Multiplication \n4 :Devision")
s = mathematics(num1,num2)
operators = {
    1:s.addition,
    2:s.subtraction,
    3:s.multiplication,
    4:s.division
}
choice = int(input())
print(" result is :" ,end=" ")
output = operators.get(choice ,errormessage)()
print(output)