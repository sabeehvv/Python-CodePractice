# def sorting(array, limit):
#     for x in range(limit):
#         for y in range(x+1, limit):
#             if array[y] > array[x]:
#                 (array[y], array[x]) = (array[x], array[y])




def sorting(arr1, limit):
    for i in range(limit):
        for j in range(i+1 , limit):
            if arr1[i] < arr1[j]:
                arr1[i],arr1[j] = arr1[j],arr1[i]
    return arr1


array1 = []
limit = int(input("Enter the size of array : "))
print("Enter the values of array\n")
for i in range(limit):
    values = int(input())
    array1.append(values)
sorting(array1, limit)
print("sorted array :")
print(array1)