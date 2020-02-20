"""
 After flipping a coin 10 times you got this result,

   result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

 Using for loop figure out count for “heads”

"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total=0
for i in result:
	if i=="heads":
		total=total+1
	else:
		continue
print(total)