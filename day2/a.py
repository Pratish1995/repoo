print "Enter rows of square matrix (odd)"
m=int(raw_input())
n=m
i=1
j=n-5
for i in range(0,m):
	if(i==0):
		print "*"+" "*(n-2)+"*"
	elif(i==m/2):
		if(m%2!=0):
			print "*"+" "*(n/2-1)+"*"+" "*(n/2-1)+"*"
		else:
			print "*"+" "*(n/2-2)+"*"+" "*(n/2-1)+"*"
	elif(i<m/2):	
		print "*"+" "*(i-1)+"*"+" "*(j+1)+"*"+" "*(i-1)+"*"
		j=j-2
	else:
		print "*"+" "*(n-2)+"*"
	i=i+1
	
		
		