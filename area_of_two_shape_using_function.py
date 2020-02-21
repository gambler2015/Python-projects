def area(l, b, shape='triangle'):
	if shape=='triangle':
		return (1/2)*l*b
	elif shape=='rectangle':
		return l*b
	else:
		return -1
triangle=area(5, 6, 'triangle')
print(triangle)