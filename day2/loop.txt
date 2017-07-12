import re
a=raw_input()

if not re.search("[aeiou]",a):
	print "C"
else:
	print "V"



