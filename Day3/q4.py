# 4)Write program to Extract elements with a Frequency greater than K

list1=[10,20,30,40,30,50,50,60,50,30]
k=2
lst=[]
dict1={}
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for keys,values in dict1.items():
    if values>k:
        lst.append(keys)
print(lst)

# Second Method
def count(list,k):
    cnt=0
    for i in range(len(list)):
        if list[i]==k:
            cnt+=1
    return cnt
list2=[10,20,30,40,30,50,50,60,50,30]
k1=2
new=[]
for i  in list2:
    freq=count(list2,i)
    if freq>k1 and i not in new:
        new.append(i)
print(new)