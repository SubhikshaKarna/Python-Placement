#Swap at given Position
def swap(lst,pos1,pos2):
    temp=lst[pos1]
    lst[pos1]=lst[pos2]
    lst[pos2]=temp
    return lst
thislist=[1,2,3,4,5]
pos1,pos2=1,3
list=[]
print(thislist)
list=swap(thislist,pos1-1,pos2-1)
print(list)
