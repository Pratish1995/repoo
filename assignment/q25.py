a=raw_input()
b=a.find("@")
c=a.find(".")
while(b<(c-1)):
	print a[b+1],
	b=b+1