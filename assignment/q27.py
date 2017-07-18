a=(1,2,3,4,5,6,7,8,9,10)
i=0
j=0
b=[]
while(i<len(a)):
	if(a[i]%2==0):
		b[j]=a[i]
		j=j+1
	i=i+1
print b