def onefunc(function):
    text = function()
    return text.upper()

def word():
    return "helo world"


output = onefunc(word)
print(output)



