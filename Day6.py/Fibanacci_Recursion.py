#Printing Fibonacci Series for Using Recursion 0(2**n)
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=5
result=fibonacci(n)
print(f"the {n}th Fibonacci Number is:",result)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 5
result = fibonacci(n)
print(f"The {n}th Fibonacci Number is:", result)
