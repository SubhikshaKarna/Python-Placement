#print all items by index number
thislist=["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#print all items without index number
thislist=["apple","banana","cherry"]
for i in thislist:
    print(i)

#print all items using while loop
thislist=["apple","banana","cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#Comprehension offers the shortest syntax for loop
#[expression for item in iterable if condition ]
thislist=["apple","banana","cherry"]
[print(x) for x in thislist]

#Based on a list of fruits, you want a new list,Conataining "a" in it
fruits=["apple","banana","cherry","Kiwi","mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#Above using list Comprehension
newlist=[x for x in fruits if "a" in x] 
print(newlist)