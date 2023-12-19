array = [[2,3,4],[2,3,4],[3,3,2],[2,3,4]]
num = len(array[0])
print(num)

num = [1,2,3,4]

lenght = len(num)
while (lenght>0):
    print(num[lenght-1], end=" ")
    lenght-=1
print()

h = lambda x:x*x
print(h(5))


import moduletrail
moduletrail.message("sabeeh")

file = open("newfile.txt", "w")

file.close()


def print5():
    print(5)
print5()


def outefunction(innerfunction):
    innerfunction()
    print("Hello world")

def newmessage():
    print("Good thinks happened here")

outefunction(newmessage)