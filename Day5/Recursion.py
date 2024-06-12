def power(N,P):
    if P==0:
        return 1
    #Recurrence relation 
    return (N*power(N,P-1))

#Driver Code
N=5
P=2
print(power(N,P))
