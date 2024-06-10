def count(list,k):
    cnt=0
    for i in range(len(list)):
        if list[i]==k:
            cnt+=1
    return cnt
list1=[10,20,30,40,30,50,50,60,50]
x=30
c=count(list1,x)
print("Count=",c)