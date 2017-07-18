import re
print "Enter passwords separated by comma"
p=raw_input()
b=p.split(",")
i=0
while(i<len(b)):
	x = True
	while x:  
		if (len(b[i])<6 or len(b[i])>12):
			break
		elif not re.search("[a-z]",b[i]):
			break
		elif not re.search("[0-9]",b[i]):
			break
		elif not re.search("[A-Z]",b[i]):
			break
		elif not re.search("[$#@]",b[i]):
			break
		else:
			print b[i]
			break
	i=i+1
