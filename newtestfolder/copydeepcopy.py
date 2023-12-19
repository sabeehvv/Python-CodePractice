import copy

listsd1 = [[1,2,3,4,5,6],[5,4,3,2,1,6,],[7,6,5,4,3,2,2]]

listsingle = [1,2,3,4,5,6]

listsingle.append(333)
listsingle.insert(4,33)

listsd2 = copy.deepcopy(listsd1)
listsd4 = listsd1.copy()
listsd5 = listsingle.copy()

listsd1[1][3]=223
listsingle[2] = 100


print(listsingle)
print(listsd5)
print(listsd1)
print(listsd2)
print(listsd4)