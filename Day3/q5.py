# 5)Write a program to Test if a list contains Elements in the range
s=2
e=6
list1=[3,4,2,1,5,7,6,9,8,10]
r=1
for i in list1:
    if  i<s or i>e:
        r=0
        break
if r==1:
    print("Contains")
elif r==0:
    print("Doesn't " )