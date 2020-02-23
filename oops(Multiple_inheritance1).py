# program that have same methods as name in base class.
class father:
	def skills(self):
		print("I am an English Teacher")
class mother:
	def skills(self):
		print("I am housewife")
class child(father,mother):
	def skills(self):
		father.skills(self)
		mother.skills(self)
		print("I am a student")

c=child()
c.skills()