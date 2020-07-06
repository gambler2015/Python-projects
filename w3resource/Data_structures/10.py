# 10. Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
#Expected output:
#[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]

from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
d=defaultdict(list) # it provides values in the list.
for i,j in class_roll:
    d[i].append(j)
print(d)
print(sorted(d.items()))
print(d.values())
