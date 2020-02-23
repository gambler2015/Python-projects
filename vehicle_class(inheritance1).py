class vehicle:
	def general_usage(self):
		print("general use")

class car(vehicle):
	def __init__(self):
		self.general_usage() # can be use here to access to base class
		print("i'm a car")
		self.wheels=4
		self.has_roof=True
	def specific_usage(self):
		print("Specific use: commute to work, vacation with famly")
class Motorcycle(vehicle):
	def __init__(self):
		self.general_usage()
		print("I'm a Motorcycle")
		self.wheels=2
		self.has_roof=False
	def specific_usage(self):
		print("Specific use: Racing")

c= car()         #c is object of car class
c.specific_usage()
m=Motorcycle()
m.specific_usage()
t=isinstance(c, car)
print(t)
print(isinstance(m, Motorcycle))
print(isinstance(m, car))
print(issubclass(car, vehicle))
print(issubclass(Motorcycle, car))