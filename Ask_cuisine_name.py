# Write a Program that asks users to enter dish name and it should print which cuisine is that dish.



Chinies=["Spring Rolls","Fried Shrimps", "Chowmein", "Dumplings", "Fried Rice", "Egg Fried Rice", "Noodle Soup", "Soy egg", "Egg Rolls"]
Indians=["Briyani", "Samosa", "Butter Chicken", "Tandoori Chicken", "Panipuri", "Naan", "Roti", "Gulab Jamun", "Momo", "Rasgulla", "Laddu", "Dosa", "Chana Masala"]
Italians=["Pizza", "Bottarga", "Lasagne", "Ribollita", "Ossobuco", "Pasta"]
Americans=["Hamburger", "Apple Pie", "Goetta", "Hot Dogs", "Gumbo", "Tex Mex", "London Broil"]
British=["Beef Wellington", "Cobbler", "Black peas"]
dish = input("Enter your dish name: ")
if dish in Indians:
	print("Your dish is Indian!")
elif dish in Italians:
	print("Your dish is Italian!")
elif dish in Chinies:
	print("Your dish is Chinies!")
elif dish in Americans:
	print("Your dish is Americans!")
elif dish in British:
	print("Your dish is British!")
else:
	print("Sorry!!! this dish is not Available")
