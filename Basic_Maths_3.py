n=int(input())
rev=0
n_cpy=n
while(n>0):
    rev=rev*10+n%10
    n=n//10
if(n_cpy==rev):
    print("Palindrome")
else:
    print("Not Palindrome")
