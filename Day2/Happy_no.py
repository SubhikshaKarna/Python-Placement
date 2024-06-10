def ishappy(num):
    sum=0
    while(num>0):
        r=num%10
        sum=sum+(r**2)
        num=num//10
    return sum
num=int(input("Enter A Number:"))
res=num
while res!=1 and res!=4:
   res=ishappy(res)
if res==1:
    print("Happy")
elif res==4:
    print("Not Happy")



