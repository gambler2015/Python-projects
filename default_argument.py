def sum(a,b=0): # if we use 2nd argument as zero. this will become default value(zero) for specifc variable
	total=a+b
	return total
s=sum(2) # if we are not paasing 2nd argmt then we have to use b=0 in function argument
print(s)
s=sum(2,8) # we can use 2nd argumnt even if b=0. it autometically make b = 8
print(s)