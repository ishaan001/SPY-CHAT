from globals import friend_age,friend_name,friend_rating
def add_friend():
    f_name = raw_input("enter your name :")

    while (f_name.isalpha() == False):
        print "name cannot be numeric"
        f_name = raw_input("enter name :")

    while (True):
        f_sal = raw_input("enter salutation what should we call you Mr/Ms. :")
        if (f_sal == "Mr" or f_sal == "Ms"):
            f_name=f_sal+"."+f_name
            print "hello you friend name is %s"%(f_name)
            break
        else:
            print "salutation not provided correctly"

    while (True):
        try:
            f_age = int(raw_input("enter age :"))
            if (f_age > 12 and f_age <50):
                print "your friend age age is " + str(f_age)
                break
            else:
                print "age cannot be less than 12 and greater tha 50"
        except Exception:
            print "invalid age" + str(Exception)

    while (True):
        try:
            f_rating = float(raw_input("enter friend rating :"))
            if (f_rating <= 5.0):
                print "your friend rating is " + str(f_rating)
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating" + Exception
    friend_name.append(f_name)
    friend_age.append(f_age)
    friend_rating.append(friend_rating)
    return len(friend_name)
