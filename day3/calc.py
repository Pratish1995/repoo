def add(a,b):
	"""add function"""
	c=a+b
	print c

def sub(a,b):
	"""sub function"""
	c=a-b
	print c

def div(a,b):
	"""division function"""
	if(a==0 and b==0):
		print "both numbers cant be zero enter again"
	elif(b==0):
		print "not defined"
	else:	
		c=a/b
		print c

def mul(a,b):
	"""mulitply function"""
	c=a*b
	print c

def mod(a,b):
	"""modulus function"""
	if(a==0 and b==0):
		print "both numbers cant be zero enter again"
	elif(b==0):
		print "not defined"
	else:	
		c=a%b
		print c
co=1
while(co==1):
	print "Enter Number 1"
	a=float(raw_input())
	print "Enter Number 2"
	b=float(raw_input())
	print "1:Add"
	print "2:Subtract"
	print "3:Multiply"
	print "4:Division"
	print "5:modulus"
	print "Choose the operation"
	n=int(raw_input())
	if(n==1):
		add(a,b)
	elif(n==2):
		sub(a,b)
	elif(n==3):
		mul(a,b)
	elif(n==4):
		div(a,b)
	elif(n==4):
		mod(a,b)
	print "Press 1 to continue and 0 to exit"
	d=int(raw_input())
	co=d
		



