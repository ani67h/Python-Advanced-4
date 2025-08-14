set1 = {0,2,1,4,6,9,9}
set2 = {2,8,9,2,7,3,5,6,4}

print('The first set is ',set1)
print('The second set is ',set2)

print(set.difference(set1)) # elements that set 1 have but set 2 doesn't have
print(set.difference(set2)) # elements that set 2 have and set 1 doesn't have

# symmetric difference = union - intersection
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1)) 