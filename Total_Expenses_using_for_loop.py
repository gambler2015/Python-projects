# find expenses in all given months and also total expenses.

exp=[1200, 1240, 2100, 2300, 5470, 2210]
"""total=0
for i in exp:
	total = total + i
print(total)
"""
total=0
for i in range(len(exp)):
	print("Month :", i+1, "Expense: ", exp[i])
	total = total+exp[i]
print("Total Expenses: ", total)