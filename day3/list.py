def checkd(a):
	listw=['monday','tuesday','wednesday','thursday','friday','saturday']
	flag=1
	for i in range(len(listw)):
		if(a==listw[i]):
			print i+1
			flag=0 
	if(flag==1):
		print "not valid"

def check(b):
	listm=['january','february','march','april','may','june','july','august','september','october','november','december']
	flag=1
	for j in range(len(listm)):
		if(b==listm[j]):
			print j+1
			flag=0
	if(flag==1):
		print "not valid" 

print "Enter A day"
m=raw_input()
n=m.lower()
checkd(n)
print "Enter a month"
a=raw_input()
b=a.lower()
check(b)
