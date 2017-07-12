print "1:Celsius \n 2:Fahrenheit\n"
a=int(raw_input())
print "Enter the temp"
b=float(raw_input())
c=0
if(a==1):
	c=b*float(1.8)+32
else:
	c=float(b-32)/1.8
print c		