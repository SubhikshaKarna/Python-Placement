# Time Complexity is O(p)
"""def power(N,P):
    if P==0:
        return 1
    #Recurrence relation 
    return (N*power(N,P-1))

#Driver Code
N=5
P=2
print(power(N,P))"""

# Time Complexity is O(logp)
def pow(n,p):
    if(p==1):
        return n
    temp=pow(n,p//2)
    if(p%2!=0):
        return n*temp*temp
    else:
        return temp*temp
n=int(input("Enter n Value:"))
p=int(input("Enter p Value:"))
print(pow(n,p))
