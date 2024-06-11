# 8)Find the Largest subarray sum of a given list 

def large_subarray(lst):
    cur_sum=max_sum=lst[0]
    for i in lst[1:]:
        cur_sum=max(i,cur_sum+i)
        max_sum=max(cur_sum,max_sum)
    return max_sum

list1=[-2,1,-3,4,-1,2,1,-5,4]
print(large_subarray(list1))