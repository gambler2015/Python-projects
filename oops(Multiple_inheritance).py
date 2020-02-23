class father:
	def teacher(self):
		print("I am an English Teacher")
class mother:
	def housewife(self):
		print("I am housewife")
class child(father,mother):
	def student(self):
		print("I am a student")

c=child()
c.teacher()
c.housewife()
c.student()