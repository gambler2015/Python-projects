"""
Write a function called add_and_multiply that takes two numbers as input and 
it should return sum and multiplication as two separate numbers.
"""
import os
def add_and_multiply(a, b):
	add=a+b
	multiply=a*b
	return add, multiply;
c, d=map(int, input().split()) #here i'm using map function to to make values integer
k, n=add_and_multiply(c, d)
print("Sum is: ",k)
print("Multiply is:",n)