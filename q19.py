#19.Write a Program to Create a Class in which One Method Accepts a String from the User and Another Prints it

class string:
	
	def input(self):
		print "enter a string"
		global a
		a=raw_input()
	def prints(self):
		print a

o=string()
o.input()
o.prints()