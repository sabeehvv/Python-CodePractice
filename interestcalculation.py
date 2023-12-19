print("Calculating Interest")
print("____________________\n\n")
P = int(input("Enter principal amount : "))
R = float(input("Enter Interest rate : "))
n = int(input("Enter number of years : "))

SI = (P*R*n)/100
print("Interest is :"+str(SI))
