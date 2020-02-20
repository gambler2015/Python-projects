#Search for lost Cell Phone in home and when you found stop searching.


key_location="Toilet"
home=["living_area", "Terris", "Bed_room", "Kitchen", "Balcony", "Master_bedroom", "Hall", "Toilet", "Reading_room"]
for i in home:
	if i==key_location:
		print("Cell Phone found in", i)
		break
	else:
		print("Cell Phone not found in location", i)