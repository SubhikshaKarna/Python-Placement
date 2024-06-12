#Write a program to Reverse a string

def reverse_str(str):
    rstr=""
    i=len(str)-1
    while(i>=0):
        rstr=rstr+str[i]
        i-=1
    return rstr
s=input("Enter the String:")
print(reverse_str(s))
