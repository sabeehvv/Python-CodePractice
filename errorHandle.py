class customexception(Exception):
    pass

class Error(customexception):
    pass

while True:
    try:
        name = str(input("Enter your last Name : "))
        if name != "sabeeh":
            raise Error
        break
    except Error:
        print("Entered Name is Invalid")

print("Validated, Your Data is Saved Successfully")