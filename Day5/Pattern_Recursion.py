def print_pattern(n,m):
    if n==0:
        return
    for i in range(k,m-1,-1):
        print(i,end="")
    print()
    print_pattern(n-1,m+1)

n=7
k=7
print_pattern(n,1)