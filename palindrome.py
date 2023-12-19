num = 0
word = str(input("Enter a String : "))
for x in range(0,int(len(word)/2)):
    if word[x] != word[len(word)-x-1]:num=1
    else:num = 0

if num == 1 :print("Entered string is not a palindrome")
else:print("Entered string is a palindrome")