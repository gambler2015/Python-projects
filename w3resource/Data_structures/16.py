#Write a Python program to convert an array to an ordinary list
#with the same items.
#Expected Output:
#Original array:
#array('b', [1, 2, 3, 4])
#Array to list:
#[1, 2, 3, 4]

from array import array
a=array('b',[1,2,3,4])
print("Original array:\n{}".format(a))
b=list(a)
print("Array to lsit:\n{}".format(b))
