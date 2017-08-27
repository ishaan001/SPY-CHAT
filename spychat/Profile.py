from start_chat import start_chat
name = None
sal = None
age = 0
rating = 0.0
message = None
Spy_onl9=False
def Take_profile():

    name = raw_input("enter your name :")

    while (name.isalpha() == False):
        print "name cannot be numeric"
        name = raw_input("enter name :")

    while(True):
        sal = raw_input("enter salutation what should we call you Mr/Ms. :")
        if (sal == "Mr" or sal == "Ms"):
            print "hello " + sal + "." + name
            break
        else:
            print "salutation not provided correctly"

    while (True):
        try:
            age = int(raw_input("enter age :"))
            if (age > 0):
                print "your age is " + str(age)
                break
            else:
                print "age cannot be 0"
        except Exception:
            print "invalid age" + str(Exception)

    while (True):
        try:
            rating = float(raw_input("enter rating :"))
            if(rating <= 5.0):
                print "your rating is " + str(rating)
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating" + Exception
    spy_onl9=True
    start_chat(name,age,rating)





