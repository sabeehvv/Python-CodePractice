def sample(funcin):
    text = funcin()
    return text.upper()

def newfinction():
    return "this is one of the text"

output = sample(newfinction)
print(output)

def onefunc(function):
    text = function()
    return text.upper()

def word():
    return "helo world"


output = onefunc(word)
print(output)


def outerfunc(func):
    func()
    print(" is name and i'm very ")



def simple(func):
    def innerfunc():
        text = func()
        return text.upper()
    return innerfunc

# @outerfunc
# def outersample():
#     print("Good Morning")

# output2 = outersample()
# print(output2)

def testing(num):
    return num ** 3
print(list(map(testing, [1,2,4,5,6]))) 


def another(functions):
    text = functions()
    return text.upper()

def letter():
    return "Good vibes"

sub = abs(-2)

print(sub)

print(another(letter))

lists = [1,2,3,4,5,6]

print([num *3 for num in lists])


def outerfuncti(functui):
    def halo_guys(l):
        text = functui(l)
        return text
    return halo_guys

newvar = [2,3,4,5,6,7]
print(newvar[::-1])


def mainfu():
    def onefung():
        global text
        text = "helllo one"

    def twofuhjgk():
        text = "helo two"

    def three():
        text = "hello three"

    text = "outer of innner function"

    onefung()
    print(text)


mainfu()

print(text)

class Newclass:

    newstaticvarv = 234
    def __init__(self,name1,name2) -> None:
        self.name11 = name1
        self.name22 = name2

    def sameclass(self):
        print(self.name11)
        print(Newclass.newstaticvarv)

    @classmethod
    def newfubctuj(ss):
        ss.newfubctuj=ss.newstaticvarv+2

namea= "first"
nameb = "Seccond"
obj =Newclass(namea,nameb)

obj.sameclass()

print(Newclass.newstaticvarv)


obj.newfubctuj() 
print(obj.newfubctuj)



def somthing(fun):
    text = fun()
    return text.upper()

def word():
    return 'sabeeh'

print(somthing(word))

def newdec(fun):
    def innerfu(num):
        outps = fun(num)
        return [item *3 for item in outps]
    return innerfu

@newdec
def newteam(numlist):
    return numlist[::-1]

print(newteam([1,2,3,4,51,11]))

