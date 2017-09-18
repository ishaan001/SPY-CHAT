import re
'''import check

question = "Continue as Mr. Ishan (Y/N)?"
existing = raw_input(question)
if(existing.upper() == "Y"):
      print "haven't designed this part yet"
else:
    check.Take_profile()
'''
pattern='^[0-9a-zA-Z]+\.jpg$'
name=raw_input("enter your age")
if(re.match(pattern,name)):
    print "done"
else:
    print "not done"



