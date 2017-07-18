import re
def validate(s):
  x = True
  while x:  
     if (len(p)<6 or len(p)>12):
         break
     elif not re.search("[a-z]",s):
         break
     elif not re.search("[0-9]",s):
         break
     elif not re.search("[A-Z]",s):
         break
     elif not re.search("[$#@]",s):
         break
     else:
         print("Valid Password")
         x=False
         break

  if x:
     print("Not a Valid Password")


print("Enter The Password:")
p= raw_input()
validate(p)