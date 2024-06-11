# filter function

original_tuple=(1,2,3,4,5)
filtered_tuple=tuple(filter(lambda x:x%2==0,original_tuple))
print("Filtered tuple:",filtered_tuple)

# reduce function
from functools import reduce

# Define a function to add 2 NUmbers
def add(x,y):
    return x+y

# Define the Original tuple
original_tuple=(1,2,3,4,5)

#Reduce the Tuple to a single value (sum of elements)

result=reduce(add,original_tuple)
print("Result of Reducing the tuple:",result)