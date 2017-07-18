#q11 and 12

import logging

a = [6,6,12,18,30]
i=1
for i in range(0,len(a)-3):
	if(a[i]+a[i+1]==a[i+2]):
		x=1
		logging.info("working")
	else:
		x=0
		break

if(x==1):
	print("The sequence is additive")
else:
	print("The sequence is not additive"