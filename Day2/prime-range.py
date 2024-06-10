start=int(input("Enter the Starting Range :"))
end=int(input("Enter the Ending Range :"))
count=0
for num in range(start,end+1):
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    else:
        print(num)
        count=count+1
print("Count=",count)