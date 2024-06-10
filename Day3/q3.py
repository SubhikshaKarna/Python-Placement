# 3)Find out the duplicate removal list product using list comprehension 
list1=[10,20,30,40,30,50,50,60,50]
seen=[]
p=1
[seen.append(list1[i]) for i in range(len(list1)) if list1[i] not in seen]
print(str(seen))
for x in seen:
    p=p*x
print("Product",p)
 