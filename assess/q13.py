#q13

print "Enter a number"
a=int(raw_input())
while(a!=1):
	if(a%2==0):
		a=a/2
		print a,
	else:
		a=3*a+1
		print a,
