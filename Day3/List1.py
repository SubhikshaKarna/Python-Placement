l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True,False]
l4=list(("Jack"))
l5=list(("Jack","John"))

print(l4)
print(l5)
print(l1[0])
print(l1[0:4])
print(l1[:4])
print(l1[0:])
print(l1[:])

#starting Index Should be less than or Equal to 0 

print(l1[-4:-1])
print(l1[-1:-4])
x=len(l1)
print(x)
print(type(l1))
print(type(l1[0]))
if "apple" in l1:
    print("Exists")

l1[1]="Kiwi"
print(l1)
l1[1:3]=["Pineapple","Dates","x"]
print(l1)

#If you Insert More than you replace

list=["apple","banana","cherry"]
list[1:2]=["blackcurrant","watermelon"]
print(list)

list=["apple","banana","cherry"]
list[1:3]=["watermelon"]
print(list)
