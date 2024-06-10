
# Check if Number is Neon or not

num=int(input("Enter the Number:"))
square=num*num
sum1=0
while square>0:
    r=square%10
    sum1=sum1+r
    square=square//10
if(sum1==num):
    print("Neon")
else:
    print("Not Neon")