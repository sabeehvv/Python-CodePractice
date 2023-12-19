def Samplefib(limit):
    a,b = 0,1
    while a < limit:
        yield a 
        a,b = b,a+b

for value in Samplefib(20):
    print(value, end=" ")

print()

listofthings = ('good','bad','wrong','happens')
lists = iter(listofthings)

print(next(lists))
print(next(lists))



def samplegen(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b
        
def samplegeneg(limit):
    a,b = 1,4
    while a < limit:
        yield a
        a,b = a+1,b+1

for valu in samplegeneg(10):
    print(valu, end=' ')

