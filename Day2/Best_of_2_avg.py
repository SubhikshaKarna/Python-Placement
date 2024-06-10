m1=int(input("Enter Mark1:"))
m2=int(input("Enter Mark2:"))
m3=int(input("Enter Mark3:"))
avg1=(m1+m2)/2
avg2=(m2+m3)/2
avg3=(m1+m3)/2
print(avg1)
print(avg2)
print(avg3)
print("Best Average of 2 Marks is:")
if avg1>avg2 and avg1>avg3:
    print(avg1)
elif avg2>avg1 and avg2>avg1:
    print(avg2)
else:
    print(avg3)