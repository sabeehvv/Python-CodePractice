def getarray():
    array= []
    print("Enter the values of array")
    for i in range (limit):
        values = int(input())
        array.append(values)
    return array

def displayarray():
    print("Entered arrays are :")
    for i in range(limit):
        print(array[i], end="\t")

limit = int(input("Enter the size of array : "))
array = getarray()
displayarray()