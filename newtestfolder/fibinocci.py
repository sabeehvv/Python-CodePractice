# def gensample(limit):
#     a,b = 0,1
#     while a < limit:
#         a,b = b, a+b
#         yield a

# for value in gensample(5):
#     print(value , end=" ")



def generator(limit):
    a , b = 0 , 1
    for i in range(limit):
        a , b = b , a + b
        yield a

for value in generator(5):
    print(value , end=" ")