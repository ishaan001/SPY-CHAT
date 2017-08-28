from globals import friends

def select_friend():
    #function to select friend from the to whom we have to send a secret message
    counter=1
    while(True):
        for friend in friends:
            print str(counter)+". "+friend['salutation']+". "+friend['name']+"\n"
            counter=counter+1
        try:
            question=int(raw_input("Select the friend to whom you want to send the message"))
            if(len(friend) >= question):
                user_input=question-1
                break


            else:
                print "No Such user Exist !"
        except Exception:
            print "invalid input"
    return user_input