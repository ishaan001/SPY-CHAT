from start_chat import start_chat
from default_spy_details import spy
import Profile
while(True):
    print "Hey ! Welcome back Lets get started"
    question = "Continue as "+spy["salutation"]+". "+spy["name"]+" (Y/N)"
    existing = raw_input(question)
    if(existing.upper() == "Y"):
        spy["status"]=True
        print "hello"+ spy["salutation"]+". "+spy["name"]
        print "\n GLAD TO HAVE TO BACK"
        start_chat(spy["name"],spy["age"],spy["rating"],spy["status"])
        break
    elif(existing.upper() == "N"):
        Profile.Take_profile("")
        break
    else:
        print "Invalid input"

