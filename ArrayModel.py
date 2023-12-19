limit1 = int(input("Enter the size of array 1 : "))
array1 = []
print("Enter the values : \n")
for x in range(0 , limit1):
    values = int(input())
    array1.append(values)
    array2 = array1.copy()
    array2.insert(2 , 60)
print ("Array 1 : "+str(array1))
print ("Array 2 : "+str(array2))