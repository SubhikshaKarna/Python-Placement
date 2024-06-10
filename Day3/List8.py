#To swap first and last element in a list
def swap(lst):
    temp=lst[0]
    lst[0]=lst[-1]
    lst[-1]=temp
    return lst
thislist=[1,2,3,4,5]
list=[]
print(thislist)
list=swap(thislist)
print(list)