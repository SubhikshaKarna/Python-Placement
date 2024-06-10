# Find Factorial of given number

num=int(input("Enter a number:"))
if num<0:
    print("No Factorial for Negative Number ")
elif num==0:
    print(num)
else:
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i=i+1
    print(fact)