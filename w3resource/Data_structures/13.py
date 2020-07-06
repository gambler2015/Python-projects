#Write a Python program to get the array size of types unsigned integer
#and float.
#Expected Output:
#4
#4
from array import array
array1=array('I', (12,25))
print(array1.itemsize)
array2=array('f', (12.2,13.78))
print(array2.itemsize)
