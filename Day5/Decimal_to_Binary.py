#Program to Convert decimal to Binary

def decimal_to_binary(d):
    if d==0:
        return "0"
    b=""
    while d>0:
        b=str(d%2)+b
        d=d//2
    return b

d=int(input("Enter a decimal number:"))
b=decimal_to_binary(d)
print("Binary representation:",b)
