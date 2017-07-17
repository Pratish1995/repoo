##18.Write a Program to Append, Delete and Display Elements of a List Using Classes

class listsss:
	def appends(self,x):
		print "enter a element to append"
		a=raw_input()
		x.append(a)
		print x
		
	def delete(self,x):
		print "enter the element to remove"
		a=raw_input()
		x.remove(a)
		print x
	
	def disp(self,x):
		print x


o=listsss()
print "enter a string"
a=raw_input()
b=list(a)

o.disp(b)
o.appends(b)
o.delete(b)