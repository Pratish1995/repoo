#q1

#if a user enters a string he get exception

print "Enter a integer"
try:
	a=int(raw_input())
except Exception as e:
	print "Enter a integer only"