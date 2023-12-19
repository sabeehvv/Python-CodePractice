class ArrayOperations:
    def getArray(self,limit,array1,array2):
        print("Enter the values of array 1\n")
        for i in range(limit):
            temp = []
            for j in range(limit):
                temp.append(int(input()))
            array1.append(temp)
            
        print("Enter the values of array 2\n")
        for i in range(limit):
            temp = []
            for j in  range(limit):
                temp.append(8)
            array2.append(temp)

    def addArray(self,limit,array1,array2):
        for i in range(limit):
            sumarray.append([0]*limit)
        for i in range (limit):
            for j in range (limit):
                sumarray[i][j]=array1[i][j]+array2[i][j]
        return sumarray
    def displayArray(self,limit,sumarray):
        print("Sum of array 1 and array 2:")
        for i in range(limit):
            for j in range(limit):
                print(sumarray[i][j], end="\t")
            print()

arraybox = ArrayOperations()

limit = int(input("Enter the size of array : "))
array1 = []
array2 = []
sumarray = []


arraybox.getArray(limit,array1,array2)
sumarray = arraybox.addArray(limit,array1,array2)
arraybox.displayArray(limit,sumarray)