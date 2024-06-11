# 9)Write a program to partition a list  around a given value such that all 
#elements less than the given value come before it and all elements greater
#than it come after it

def partition(lst,pivot):
    l=[x for x in lst if x<pivot]
    e=[x for x in lst if x==pivot]
    g=[x for x in lst if x>pivot]
    return l+e+g


list=[3,1,4,1,5,9,2,6,5]
pivot_value=4
print(partition(list,pivot_value))
