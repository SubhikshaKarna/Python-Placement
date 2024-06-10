# 7)To Merge 2 sorted list into a single sorted list
lst1=[1,3,6,8]
lst2=[4,9,7]
lst1.extend(lst2)
lst1.sort()
print(lst1)


# Second Method
list1=[1,2,6,8]
list2=[3,4,9,7]
m=[]
i=j=0
while(i<len(list1) and j<len(list2)):
    if list1[i]<list2[j]:
        m.append(list1[i])
        i=i+1
    else:
        m.append(list2[j])
        j=j+1
m.extend(list2[j:])
m.extend(list2[i:])
print(m)
