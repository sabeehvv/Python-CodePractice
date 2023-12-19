def triple(func):
    def wrapper(l):
        result = func(l)
        return [item / 2 for item in result]
    return wrapper


@triple
def reverse(num):
    return num[::-1]


print(reverse([6,66,46,56,6]))


def simple(func):
    def wrapper():
        text = func()
        return text.upper()
    return wrapper

def word():
    return "HEllo my dear"

output = simple(word)

print(output)

from datetime import datetime