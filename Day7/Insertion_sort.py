def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        #Move elements of arr[0...,i-1],that are greater than key 
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[64,25,12,22,11]
insertionSort(arr)
print(arr)


