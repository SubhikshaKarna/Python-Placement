tuple_of_tuples=((1,'apple'),(3,'orange'),(2,'banana'))
sorted_tuples=sorted(tuple_of_tuples,key=lambda x:x[1])
print("Sorted tuples:",sorted_tuples)