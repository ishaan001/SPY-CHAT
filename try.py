import random
ch=raw_input("guess a letter between EVAPORATE :")
value=random.choice('EVAPORATE')
print value
if ch == value :
    print "guessed correctly"
else:
    print "guessed incorrectly"

i=raw_input("enter a phrase :")
if i.strip():
    i=i.strip()
    print i
else:
    print "hie"

