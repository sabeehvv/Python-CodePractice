def triple(func):
    def wrapper(l):
        outer = func(l)
        return [item * 3 for item in outer]
    return wrapper
@triple
def listes(num):
    return num[::-1]

print(listes([1,2,3,4,5,6,7]))




unit = 43
oil = 4543
littre = 34
stringd = "Hello How are you {}, what you want{}{} ?"

print(stringd.format(unit,oil,littre))