class vehicle:
	def general_usage(self):
		print("general use")

class car(vehicle):
	def __init__(self):
		print("i'm a car")
		self.wheels=4
		self.has_roof=True
	def specific_usage(self):
		print("Specific use: commute to work, vacation with famly")
class Motorcycle(vehicle):
	def __init__(self):
		print("I'm a Motorcycle")
		self.wheels=2
		self.has_roof=False
	def specific_usage(self):
		print("Specific use: Racing")

c= car()         #c is object of car class
c.general_usage() # Can be access parent class by child class
c.specific_usage()
m=Motorcycle()
m.specific_usage()