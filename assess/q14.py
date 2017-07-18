#q12

print "enter a number"
flag=0
a=int(raw_input())
while(a!=1):
	if(a%2==0):
		a=a/2
	else:
		flag=1
		print "Not a factor of 2"
		break
if(flag==0):
	print "Factor of 2"
	
