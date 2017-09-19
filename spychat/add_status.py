import globals

def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        #this will shouw user the current message is there is any
        print "ur current status message is %s"%(current_status_message)
    else:
        print "u don't have any status message"
    while(True):
        #to give the choice to select the status from the older message
        default=raw_input("do u want to select from older message (Y/N) :")
        if(default.upper() == "Y"):
            counter=1
            z=len(globals.Status_messages)
            for x in range(z):
                print str(counter)+" "+str(globals.Status_messages[x])
                counter=counter+1
            msg_sel=int(raw_input("select from the above messages :"))
            if(len(globals.Status_messages) >= msg_sel):
                updated_status_message=globals.Status_messages[msg_sel-1]
                print "your updated status message is %s" % (updated_status_message)
                break

            break
        elif(default.upper() == "N"):
            #if user want to have a new status message and this new message should be added to current message dictionaries
            new_status_message=raw_input("enter new status message\n")
            #used strip method is used to remove the spaces from the starting and the end of the string
            if  new_status_message.strip():
                new_status_message=new_status_message.strip()

                globals.Status_messages.append(new_status_message)
                updated_status_message=new_status_message
                print "your updated status message is %s"%(updated_status_message)
                break
            else:
                print "u haven't entered any character"
        else:
            print "INVALID INPUT"
    return updated_status_message


