import datetime

print(datetime.datetime.now())

now = datetime.datetime.now


newvar = ("fds","gtre","tre")

y = list(newvar)
y.append("newvalue")

newvar = tuple(y)
print(newvar)


newlist = ("rew","fass","djfh")

seccondlist = ("newvalue",)

newlist += seccondlist

print(newlist)