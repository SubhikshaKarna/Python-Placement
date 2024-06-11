my_tuple=(1,2,3)
another_tuple=tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
combined_tuple=my_tuple+another_tuple
print(combined_tuple)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print( 2 in my_tuple) #output : True
print(4 not in my_tuple) #output: True
print(len(my_tuple)) #outpur:3
for item in my_tuple:
    print(item)
string_to_tuple=tuple("Hello")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(2)) # output:1
print(my_tuple.count(3)) #output :2