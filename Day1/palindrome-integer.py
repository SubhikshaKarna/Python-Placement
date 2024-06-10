# To Check if a Number is Palindrome or not

num=int(input("Enter the Number:"))
n=str(num)
if n==n[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")



n=int(input("Enter the Number:"))
rev=0
temp=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if(rev==temp):
    print("Palindrome")
else:
    print("Not Palindrome")
