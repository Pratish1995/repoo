 #Q19

i = raw_input("Enter the string ")

s = set(i)

for x in s:

    print x + "," + str(i.count(x))