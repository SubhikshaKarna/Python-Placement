"""# 10)Find a peak Element in a list of integers
(Peak Element is a element that is greater than or equal its neighbours)"""

def peak(lst):
    if not lst:
        return None
    l,r=0,len(lst)-1
    while(l<r):
        mid=l+(r-l)//2
        if(lst[mid]<lst[mid+1]):
            l=mid+1
        else:
            r=mid
    return lst[l]

list1=[]
n=int(input("Enter Length of List:"))
for i in range(n):
    a=int(input())
    list1.append(a)
#list1=[1,2,1,3,5,6,4]
print("Peak=",peak(list1))