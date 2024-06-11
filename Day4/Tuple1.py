def create_tuples():
    t1=(1,2,3,4,5)
    t2=('a','b','c','d','e')
    t3=("apple","banana","cherry")
    return t1,t2,t3

def access_tuple_items(t1,t2):
    print("Tuple 1:",t1)
    print("First Element of Tuple 1:",t1[0])
    print("Last Element of Tuple 1:",t1[-1])
    print("Tuple 2:",t2)
    print("Second Element of tuple 2:",t2[1])
    print("Second last element of tuple 2:",t2[-2])
    print(t1[0:5])

def unpacking_tuple1(t3):
    (green,yellow,red)=t3
    print(green)
    print(yellow)
    print(red)

def unpacking_tuple2(fruits):
    fruits=("apple","Banana","Cherry","Strawberry","raspberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)

def change_tuple1(t1,t2):
    list1=list(t1)
    list2=list(t2)
    list1.append(6)
    list2.remove('c')
    t1=tuple(list1)
    t2=tuple(list2)
    return t1,t2

def loop_through_tuple(t1):
    print("Looping through tuple 1 using for Loop:")
    for item in t1:
        print(item)
    print("\n Looping usinng while Loop and index numbers:")
    index=0
    while index <len(t1):
        print(t1[index])
        index+=1
def join_tuples(t1,t2):
    t3=t1+t2
    return t3

t1,t2,t3=create_tuples()
access_tuple_items(t1,t2)
print()

unpacking_tuple1(t3)
print()

fruits=("apple","bananna","Cherry","Strawberry","raspberry")
unpacking_tuple2(fruits)
print()

t1,t2=change_tuple1(t1,t2)
print("After Making Changes:")
access_tuple_items(t1,t2)
print()

t3=join_tuples(t1,t2)
print("Joined tuple:",t3)