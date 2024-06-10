#First and Last Element in list
list1=[10,20,30,40]
print(list1[0],list1[len(list1)-1])

# find minimum and maximum of a list
list2=[5,6,3,4,1]
list2.sort()
print(list2[0],list2[len(list2)-1])

list3=[5,6,3,4,1]
max=list3[0]
for i in range(len(list3)):
    if max<list3[i]:
        max=list3[i]
print(max)


list3=[5,6,3,4,1]
min=list3[0]
for i in range(len(list3)):
    if min>list3[i]:
        min=list3[i]
print(min)
