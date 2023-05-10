n=int(input())
term=1
sum=0
odd=1
for i in range(1,n+1,1):
    term=term+odd
    sum=sum+term
    odd=odd+2
print(sum)
