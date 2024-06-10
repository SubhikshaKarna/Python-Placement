# Check if the Number is Spy Number or not

#sum of all digits equal to product of the number

num=int(input("Enter the Number:"))
sum1=0
p=1
while num>0:
    r=num%10
    sum1=sum1+r
    p=p*r
    num=num//10
if(sum1==p):
    print("spy")
else:
    print("Not spy")