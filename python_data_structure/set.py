set1 = {1,2,3,4,4,5,6,7,7}
print(set1)

set1.add(7)
print(set1)

# union() , intersection() ,difference() ,symmertic_diff)

set2 = {3,5,6,7}

print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))