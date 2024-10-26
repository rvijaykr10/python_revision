my_set = set()
my_set.add(1)
my_set.add(100)
my_set.add(100)
my_set.remove(100)
my_set.discard(100)
my_set.clear()

new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
my_set = set(new_list)
new_set = {1, 2, 3}.copy()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)

set1.issubset(set2)
set1.issuperset(set2)
set1.isdisjoint(set2)
