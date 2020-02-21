def sum(a, b):
	total=a+b
	print(total) #locally accessed
	return total
s=sum(5, 8)
print(s)
print(total) # it can't be accessed because total is local variable only used inside the function

#........................................................................................
total=0
def sum(a, b):
	total=a+b
	print(total) # print value 3 because it is accessing local variable(total)
	return total
s=sum(1, 2)
print(s)
print(total) # print value 0 because it is accessing global variable(total)