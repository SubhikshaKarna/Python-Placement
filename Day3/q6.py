# 6)Write a program to demonstrate  list intersection and Union
list1=[1,2,6,8]
list2=[1,2,4,9,7]
lst_i= list(set(list1) & set(list2))
lst_u= list(set(list1) | set(list2))
print(lst_i)
print(lst_u)

# Second Method
list1=[1,2,6,8]
list2=[1,2,4,9,7]
m=[]
i=j=0
while(i<len(list1) and j<len(l2)):
    if list1[i]<list2[j]:
        m.append(list1[i])
