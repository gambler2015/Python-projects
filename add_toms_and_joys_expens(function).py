# Make a programe that can find total expense of tom and joy using an specific code.

toms_exp=[1200, 1300, 3011, 4211]
joys_exp=[4100,4500,1230,2291]

def calculate_exp(exp):
	total=0
	for i in exp:
		total = total+i
	return total

total_toms_exp=calculate_exp(toms_exp)
total_joys_exp=calculate_exp(joys_exp)
print(total_toms_exp)
print(total_joys_exp)