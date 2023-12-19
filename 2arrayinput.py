# limit = int(input("Enter the size of arrays : "))
# array1 = []
# array2 = []
# sumarray = []
# print("Enter the values of array 1\n")
# for x in range(limit):
#     a = []
#     for y in range(limit):
#         a.append(int(input()))
#     array1.append(a)
# print("Enter the values of array 2\n")
# for x in range(limit):
#     a = []
#     for y in range(limit):
#         a.append(int(input()))
#     array2.append(a)

# sumarray = [[array1[i][j] +array2[i][j] for j in  range (len(array1[0]))] for i in range (len(array2))]

# print( "Sum of 2 arrays is :")
# for i in range(limit):
#     for j in range(limit):
#         print(sumarray[i][j],"\t", end="")
#     print()

# print(array1)

# limit = int(input("Enter the size of array"))
# arr1 = []
# arr2 = []
# sumarray = []
# print("enter the elements of array")
# for i in range(limit):
#     arr1.append(int(input()))
# print("enter the 2nd elements of array")
# for i in range(limit):
#     arr2.append(int(input()))
# for i in range(limit):
#     sumarray.append(arr1[i] + arr2[i])
# print(sumarray)


limit = int(input("enter the limit of array"))

arr1 = []
arr2 = []
sumarr = []

print("enter the 1st elements of array")

for i in range(limit):
    a = []
    for j in range(limit):
        a.append(int(input()))
    arr1.append(a)

print("Enter the elements of 2nd array")

for i in range(limit):
    a = []
    for j in range(limit):
        a.append(int(input()))
    arr2.append(a)

for i in range(limit):
    a = []
    for j in range(limit):
        a.append(arr1[i][j] + arr2[i][j])
    sumarr.append(a)


print(arr1,arr2,sumarr)