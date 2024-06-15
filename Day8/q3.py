#An Equlibrium is a index such that the sum of Elements of lower indexes is equal sum of index in upper index
"""Example :
arr=[-7,1,5,3,2,-4,3,0]
output:3 """
# if no such point exist return -1

def Equilibrium(arr):
    n=len(arr)
    for i in range(n):
        lsum=sum(arr[0:i])
        rsum=sum(arr[i+1:n])
        if lsum==rsum:
            return i
    return -1

arr=[-7,1,5,2,-4,3,0]
res=Equilibrium(arr)
print(res)