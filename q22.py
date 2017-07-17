s = raw_input()
d=0
a=0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        a+=1
print "Digits ",
print d
print "Letters ",
print a
