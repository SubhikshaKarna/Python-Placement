#Tuple Comprehension to Create a tuple of squares
squares_tuple=tuple(x**2 for x in range(1,6))
print("Squared Tuple:",squares_tuple)

# Zip function

l1=[1,2,3]
l2=['a','b','c']
zipped_tuple=tuple(zip(l1,l2))
print("Zipped tuple:",zipped_tuple)

