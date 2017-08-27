import Profile
while(True):
    question = "Continue as Mr. Ishan (Y/N)?"
    existing = raw_input(question)
    if(existing.upper() == "Y"):
        print "haven't designed this part yet"
        break
    elif(existing.upper() == "N"):
        Profile.Take_profile()
        break
    else:
        print "Invalid input"

