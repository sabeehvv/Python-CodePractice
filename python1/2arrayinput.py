limit = int(input("enter size of array"))

arr1 = []
arr2 = []

print('Enter Array one values')

for x in range(limit):
    a = []
    for y in range(limit):
        a.append(int(input()))
    arr1.append(a)

print('enter array 2 values')
for x in range(limit):
    a = []
    for y in range(limit):
        a.append(int(input()))
    arr2.append(a)

sumarray = [[arr1[i][j] + arr2[i][j] for j in range(limit)]for i in range(limit)]

print(sumarray)