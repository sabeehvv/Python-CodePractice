a = 20
b = 30
c = 15

def funct(a,b,c):
    if a<b<c:
        return b
        
    elif b<a<c: 
        return a
    elif c<b<a:
        return b
    else: 
        return c
    
print(funct(2,4,3))