n=int(raw_input())
i=0
j=0

while(i<n):
	print "* "*j
	j=j+1
	i=i+1
	if(i==(n-1)):
		i=0
		j=n
		print "* "*j
		j=j-1
		i=i+1