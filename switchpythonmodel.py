choice = int(input("1 for Sunday\n2 for Monday\n3 for Tuesday\n4 for Wednesday\n5 for thursday\n6 for Friday\n7 for saturday \n\n Enter your choice\t:"))
days = ["Sunday","Monday","Tuesday","Wednesday","thursday","Friday","saturday"]
if(choice<=7):print("you have selected : "+ str(days[choice -1]))
else:print("Invalid Entry")