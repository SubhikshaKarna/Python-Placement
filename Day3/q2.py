# 2)Write the Program to count the unique values in the list
list1=[10,20,30,40,30,50,50,60,50]
dict1={}
count=0
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for keys,values in dict1.items():
    if values>=1:
        count+=1
print("Count of Unique Number in List =",count)


# Second Method
list1=[10,20,30,40,30,50,50,60,50]
seen=[]
for i in range(len(list1)):
    if list1[i] not in seen:
        seen.append(list1[i])
print("Count=",len(seen))
