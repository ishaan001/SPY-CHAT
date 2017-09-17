from start_chat import start_chat
from default_spy_details import spy
from colorama import init,Fore,Back
import Profile
while(True):
    init()
    print Fore.YELLOW+"Hey ! Welcome back Lets get started"
    question = "Continue as "+Fore.RED+spy.salutation+". "+spy.name+Fore.RESET+" (Y/N)"
    existing = raw_input(question)
    if(existing.upper() == "Y"):
        spy.current_status_message=True
        print "hello "+ spy.salutation+"."+spy.name
        print "\n GLAD TO HAVE TO BACK"
        start_chat(spy.name,spy.age,spy.rating,spy.is_online)
        break
    elif(existing.upper() == "N"):
        Profile.Take_profile("")
        break
    else:
        print "Invalid input"

