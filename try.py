
name = raw_input("enter your name")

while(name.isalpha()==False):
        print "name cannot be numeric"
        name=raw_input("enter name")
sal = raw_input("enter salutation")
print "hello" +sal+ "."+name
while(True):
    try :
        age =int(raw_input("enter age"))
        if(age>0):
            print "your age is "+ str(age)
            break
        else:
            print "age cannot be 0"
    except Exception :
        print "invalid age" +str(Exception)

while(True):
    try :
        rating =float(raw_input("enter rating"))
        print "your age is "+ str(rating)
        break
    except Exception :
        print "invalid rating" +Exception
message=raw_input("enter message")
print "message is"+ message