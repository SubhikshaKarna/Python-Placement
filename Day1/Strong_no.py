#sum of Factorial of individual digit is equal to the number itself

sum=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if(sum==temp):
    print("Strong")
else:
    print("Not Strong")