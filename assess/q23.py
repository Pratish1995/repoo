print "enter a string"
b=raw_input()

with open("abc.txt","a") as a:
    a.write(b)