def decoraate(func):
    def wrapper(num):
        value = func(num)
        return [item * 3 for item in value]
    return wrapper

@decoraate
def reverse(l):
    return l[::-1]

print(reverse([2,3,4,5,6,7]))