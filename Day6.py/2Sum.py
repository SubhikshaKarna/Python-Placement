"""Given an array of N Numbers and Another Number x,
The Task is to check whether or not there exist 2 numbers in array
 whose Exact sum is x"""

# Time Complexity is O(N^2)

def twoSum(nums,target):
        arr=[]
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                     return "Yes"
        return "No"
nums= [1,4,45,6,10,8]
target = 16
print(twoSum(nums,target))


# Time Complexity 
def sum(arr,x):
    c=set()
    for i in arr:
        if (x-i) in c:
            return True
        c.add(i)
    return False
arr=[1,4,45,6,10,8]
x=16
print(sum(arr,x))

#
def keyPair(arr,x):
    l=0
    r=len(arr)-1
    while(l<r):
        if arr[l]+arr[r]==x:
            return True
        elif(arr[l]+arr[r]>x):
            r-=1
        else:
            l+=1
    return False

arr=[1,4,45,6,10,8]
x=16
arr.sort()
print(keyPair(arr,x))	    