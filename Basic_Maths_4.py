M,N=int(input()),int(input())
prod_MN=M*N
min_num=min(M,N)
while(N>0):
    rem=M%N
    M=N
    N=rem
print(f"HCF={M} LCM={prod_MN//M}")
