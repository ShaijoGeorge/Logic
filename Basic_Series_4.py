n,a=int(input()),int(input())
sum=1
sign=1
j=2
for i in range(2,n+1):
    sum=sum+sign*a**j
    j=j+2
    sign*=-1
print(sum)
