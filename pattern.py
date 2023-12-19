limit = int(input("Enter pattern limit : "))
count = (limit * (limit+1)/2)+1
for i in range (limit,0,-1):
    count -= i
    for j in range(i):
        print(int(count), end="\t")
        count += 1
    count -= i
    print()
        


