#importing start_chat and spy
from start_chat import start_chat
from default_spy_details import spy

#importing from colorama for coloured
from colorama import init,Fore,Back
import Profile
while(True):
    init()
    #Asking the user that if he/she want to continue as old user or not
    print Fore.YELLOW+"Hey ! Welcome back Lets get started"
    question = "Continue as "+Fore.RED+spy.salutation+". "+spy.name+Fore.RESET+" (Y/N)"
    existing = raw_input(question)
    # Y will be considered as yes and will be continued as default user
    if(existing.upper() == "Y"):
        spy.current_status_message=True
        print "hello "+ spy.salutation+"."+spy.name
        print "\n GLAD TO HAVE TO BACK"
        start_chat(spy.name,spy.age,spy.rating,spy.is_online)
        break
    # N will be considered as No and will be continued as New user
    elif(existing.upper() == "N"):
        #this will direct them to Profile where the new user will be made
        Profile.Take_profile("")
        break
    else:
        print "Invalid input"

