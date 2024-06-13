#print first element from array O(1)
array=[1,2,3,4]
print(array[0])

#Binary Search Example for O(logn)
def Binary_Search(arr,x):
    l=0
    n=len(arr)
    r=n-1
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            l=mid+1
        else:
            r=mid-1
    return -1
a=[1,4,45,6,10,8]
k=10
a.sort()
res=Binary_Search(a,k)
if res==-1:
    print("Not Found")
else:
    print(res)

#Linear search o(n)
def Linear_Search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1

a1=[1,2,3,4,5]
k=3
res=Linear_Search(a1,3)
if res==-1:
    print("Not Found")
else:
    print(res)


#Binary Search using Recursion

def binary_search_recursion(arr,target,left,right):
    if left>right:
        return -1 #Base Case: target not found
    mid=(left+right)//2

    if arr[mid]==target:
        return mid #Target found,return its index
    elif arr[mid]<target:
        return(binary_search_recursion(arr,target,mid+1,right))
    else:
        return(binary_search_recursion(arr,target,left,mid-1))
a1=[1,2,3,4,5]
k=3
l=0
r=len(a1)-1
res=binary_search_recursion(a1,k,l,r)
if res==-1:
    print("Not Found")
else:
    print(res)

#Bubble sort O(n^2)
def Bubble_Sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
arr=[3,4,2,6,8,7]
n=6
Bubble_Sort(arr,n)
print(arr)



