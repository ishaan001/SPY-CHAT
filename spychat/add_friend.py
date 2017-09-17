from default_spy_details import Spy,friends
import re
def add_friend():
    new_friend=Spy(" "," ",0,0.0)

    while(True):
        new_friend.name= raw_input("enter your name :")
        pattern_nf = '^[A-Z]{1}[a-z\s]+$'
        if (re.match(pattern_nf, new_friend.name) != None):
            print ("your name is :" + new_friend.name)
            break
        else:
            print "name cannot be numeric and Should start with capital letter"

    while (True):
        new_friend.salutation = raw_input("enter salutation what should we call you Mr/Ms. :")
        if (new_friend.salutation == "Mr" or new_friend.salutation == "Ms"):
            f_name=new_friend.salutation+"."+new_friend.name
            print "hello you friend name is %s"%(f_name)
            break
        else:
            print "salutation not provided correctly"

    while (True):

            new_friend.age = raw_input("enter age :")
            pattern_nf_a = '^[0-9]{1,3}$'
            if (re.match(pattern_nf_a, new_friend.age) != None):
                print "your age is " + str(new_friend.age)
                new_friend.age = int(new_friend.age)
                break
            else:
                print "age cannot be 0 or alphabet"

    while (True):
        try:
            new_friend.rating = float(raw_input("enter friend rating :"))
            if (new_friend.rating <= 5.0):
                print "your friend rating is " + str(new_friend.rating)
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating it can't be string"
    new_friend.is_online=True
    friends.append(new_friend)
    print "Friend ADDED"
    return len(friends)
