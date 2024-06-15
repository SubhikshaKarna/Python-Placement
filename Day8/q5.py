#Given an array of size n-1 such that it only contains distinct integer in range 1 to n,find the missing element 
"""input
n=10
arr=[6,1,2,8,3,4,7,10,5]"""

def missing(arr,n):
    sum_n=(n*(n+1))//2
    return sum_n-sum(arr)

n=10
arr=[6,1,2,8,3,4,7,10,5]
res=missing(arr,n)
print(res)
