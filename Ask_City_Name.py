"""Write a program that uses following list of cities per country,

 uk=["Birmingham", "London", "Brisol", "Liverpool", "Nottingham", "Sheffield", "Glasgow"]

 us=["New York", "Los Angeles", "Chicago", "Houston", "Atlanta"]

 india=["Delhi", "Mumbai", "Banglore", "Kolkata"]

    (a) Write a program that asks user to enter a city name and it should tell you which country it belongs to

    (b) Write a program that asks user to enter two cities and tell you if they both are in same country or not
 """


uk=["Birmingham", "London", "Brisol", "Liverpool", "Nottingham", "Sheffield", "Glasgow"]
us=["New York", "Los Angeles", "Chicago", "Houston", "Atlanta"]
india=["Delhi", "Mumbai", "Banglore", "Kolkata"]
canada=["Toronto"]


#(a)
city=input("Enter City name to get Country: ")
if city in uk:
	print("This City is in United Kingdom")
elif city in us:
	print("This City is in United States")
elif city in india:
	print("This City is in India")
elif city in canada:
	print("This City is in Canada")
else:
	print("Not Available in our data base")


#(b)
city1, city2 = input("Enter City1,City2:").split()
if city1 and city2 in uk:
	print("Both Cities is in United Kingdom")
elif city1 and city2 in india:
	print("Both cities is in India")
elif city1 and city2 in us:
	print("Both cities is in United States")
elif city1 and city2 in canada:
	print("Both cities is in Canada")
else:
	print("Sorry!! this Data is not Available")