def hellodeca(func):
    def innerfunc(num):
        outresult = func(num)
        return [item * 3 for item in outresult]
    return innerfunc


@hellodeca
def newfunc(numbers):
    return numbers[::-1]


print(newfunc([3,8,4,5,6,]))


def argumentss(*argm):
    result = min(argm)
    return result

print(argumentss(1,2,3,4,5,6))


def anything(**best):
    result = [item for item in best]
    return result


print(anything(firstmember = "sabeeh",seccond = "aave", third = "newmember"))


def decora(func):
    def innerfun(num):
        numbe = func(num)
        return [item * 3 for item in numbe]
    return innerfun


@decora
def sample(num):
    return num[::-1]


print(sample([1,2,3,4,5]))