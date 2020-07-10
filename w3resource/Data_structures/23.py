#Write a Python program to get the two largest and three smallest items
#from a dataset.
#Expected Output:
#[100, 90]
#[0, 1, 5]

import heapq
li=[10,20,60,23,100,25,6,90,10,0,5,1,8]
print(heapq.nlargest(2, li))
print(heapq.nsmallest(3, li))
