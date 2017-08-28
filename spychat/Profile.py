from default_spy_details import spy
from start_chat import start_chat
name = None
sal = None
age = 0
rating = 0.0
message = None
def Take_profile(dict_name):

    spy["name"] = raw_input("enter your name :")

    while (spy["name"].isalpha() == False):
        print "name cannot be numeric"
        spy["name"] = raw_input("enter name :")

    while(True):
        spy["salutation"] = raw_input("enter salutation what should we call you Mr/Ms. :")
        if (spy["salutation"] == "Mr" or spy["salutation"] == "Ms"):
            print "hello " + spy["salutation"] + "." + spy["name"]
            break
        else:
            print "salutation not provided correctly"

    while (True):
        try:
            spy["age"] = int(raw_input("enter age :"))
            if (spy["age"] > 0):
                print "your age is " + str(spy["age"])
                break
            else:
                print "age cannot be 0"
        except Exception:
            print "invalid age it can only be integer"

    while (True):
        try:
            spy["rating"] = float(raw_input("enter rating :"))
            if(spy["rating"] <= 5.0):
                print "your rating is " + str(spy["rating"])
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating it can't be string"
    spy["status"]=True
    start_chat(spy["name"],spy["age"],spy["rating"],spy["status"])





