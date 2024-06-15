#Given array of interger and number k find the count of distinct elements in every window of size n in array

def count_distinct_in_windows(arr,n,k):
    result=[]
    for i in range(n-k+1):
        window=arr[i:i+k]
        distinct_count=len(set(window))
        result.append(distinct_count)
    return result 
n=int(input("Enter the Size of array:"))
arr=[]
for i in range(0,n):
    arr.append(int(input()))
k=int(input("Enter the size of the window:"))
result=count_distinct_in_windows(arr,n,k)
for count in result:
    print(count,end='\t')