set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set1={"a","b","c"}
set2={1,2,3}
set3=set1|set2
print(set3)

set1={1,4,5}
set2={1,2,3}
set3=set1.intersection(set2)
print(set3)

set1={1,4,5}
set2={1,2,3}
set3=set1 & set2
print(set3)

set1={1,4,5}
set2={1,2,3}
set1.intersection_update(set2)
print(set1)

set1={1,4,5}
set2={1,2,3}
set1.difference(set2)
print(set1)

set1={1,4,5}
set2={1,2,3}
set1.symmetric_difference(set2)
print(set1)

set1={1,4,5}
set2={1,2,3}
set1.symmetric_difference_update(set2)
print(set1)


