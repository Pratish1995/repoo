print "enter the command and the amount D or W "
final = 0
while True:
    s = raw_input()
    if not s:
        break
    a = s.split(" ")
    d = a[0]
    amt = int(a[1])
    if d=="D":
        final+=amt
    elif d=="W":
        final-=amt
    else:
        pass
print final