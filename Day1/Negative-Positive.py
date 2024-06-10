# Convert a number from Negative to Positive

num=int(input("Enter the number:"))
if num<0:
    num1=abs(num)
else:
    num1=num
print(num1)
 


num=int(input("Enter the number:"))
print(max(num,-num))