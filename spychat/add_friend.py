from globals import friends
def add_friend():
    new_friend={
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'status':False
    }
    new_friend['name'] = raw_input("enter your name :")

    while (new_friend['name'].isalpha() == False):
        print "name cannot be numeric"
        new_friend['name'] = raw_input("enter name :")

    while (True):
        new_friend['salutation'] = raw_input("enter salutation what should we call you Mr/Ms. :")
        if (new_friend['salutation'] == "Mr" or new_friend['salutation'] == "Ms"):
            f_name=new_friend['salutation']+"."+new_friend['name']
            print "hello you friend name is %s"%(f_name)
            break
        else:
            print "salutation not provided correctly"

    while (True):
        try:
            new_friend['age'] = int(raw_input("enter age :"))
            if (new_friend['age'] > 12 and new_friend['age'] <50):
                print "your friend age age is " + str(new_friend['age'])
                break
            else:
                print "age cannot be less than 12 and greater tha 50"
        except Exception:
            print "invalid age it can only be integer"

    while (True):
        try:
            f_rating = float(raw_input("enter friend rating :"))
            if (f_rating <= 5.0):
                print "your friend rating is " + str(f_rating)
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating it can't be string"
    new_friend['status']=True
    friends.append(new_friend)
    print "Friends ADDED"
    return len(friends)
