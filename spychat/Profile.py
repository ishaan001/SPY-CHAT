# importing spy and shat_chat
from default_spy_details import spy
from start_chat import start_chat
# re module imported for  regex patterns
import re
name = None
sal = None
age = 0
rating = 0.0
message = None
def Take_profile(dict_name):
    while(True):
        spy.name = raw_input("enter your friend name :")
        #regex Pattern is used for validations
        pattern_n='^[A-Z]{1}[a-z\s]+$'
        if(re.match(pattern_n,spy.name)!=None):
            print ("your name is :"+spy.name)
            break
        else:
            print "name cannot be numeric and Should start with capital letter"


    while(True):
        #validations used for salutations
        spy.salutation = raw_input("enter salutation Mr/Ms. :")
        if (spy.salutation == "Mr" or spy.salutation == "Ms"):
            print "hello " + spy.salutation + "." + spy.name
            break
        else:
            print "salutation not provided correctly"

    while (True):
            #validations for age used
            spy.age = raw_input("enter age :")
            pattern_a='^[0-9]{1,3}$'
            if (re.match(pattern_a,spy.age)!=None):
                print "your age is " + str(spy.age)
                spy.age=int(spy.age)
                break
            else:
                print "age cannot be 0 or alphabet"


    while (True):
        #validation for the rating that it should be float only
        try:
            spy.rating = float(raw_input("enter rating :"))
            if(spy.rating <= 5.0):
                print "your rating is " + str(spy.rating)
                break
            else:
                print "rating cannot be greater than 5"
        except Exception:
            print "invalid rating it can't be string"
    spy.is_online=True
    #full spy profile should be sent to start_chat for further task
    start_chat(spy.name,spy.age,spy.rating,spy.is_online)





