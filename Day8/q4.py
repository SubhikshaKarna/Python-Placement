# Your given an  MXN integer grid accounts where accounts of i and j is the amount of money the ith customer has in jth bank the customers wealth if  the amount of money they have in all the bank accounts,the richest customer , if the customer has the maximum wealth
""""list=[[1,5],[7,3],[3,5]]
output:10"""

def wealth(lst):
    max_wealth=0
    for i in lst:
        w=sum(i)
        if w>max_wealth:
            max_wealth=w
    return max_wealth


lst=[[1,5],[7,3],[3,5]]
res=wealth(lst)
print(res)

m=int(input("Enter number of Customers:"))
n=int(input("Enter number of banks:"))

accounts=[]
for i in range(m):
    print(f"Enter wealth for customer {i+1} in {n} banks:")
    customer_wealth=list(map(int,input().split()))
    accounts.append(customer_wealth)
print(wealth(accounts))

