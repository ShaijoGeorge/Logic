n=int(input())
sum=0
sign=1
for i in range(1,n+1):
    sum=sum+sign*i*i
    sign=sign*-1
print(sum)
