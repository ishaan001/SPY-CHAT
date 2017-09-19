#importing all the features of the application which are in different files
from read_chat_history import read_chat_history
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
def start_chat(name,age,rating,status):
        from globals import current_status_message
        #age should be less greater than 12 and less tah 50
        if not (age >12 and age <50):
            print "Authentication failed Please Try again Later"
        else:
            Chat_flag=True
            while(Chat_flag):
                try:
                    #choices are being given to the user
                        Menu_choices = "what do u want to do ?\n"\
                                       " 1. Add a status message ?\n"\
                                       " 2. Add a friend ?\n"\
                                       " 3. send a Secret Message.\n"\
                                       " 4. read a secret message. \n"\
                                       " 5. read chats from user.\n"\
                                       " 6. Exit Application.\n"
                        menu_choice=int(raw_input(Menu_choices))
                        if(menu_choice == 1):
                            print "u entered status message block"
                    #this will give user the access to add a status message
                            current_status_message=add_status(current_status_message)
                        elif(menu_choice == 2):
                            print "u entered add a friend block"
                    # this will give user the access to add a friend
                            Total_friends=add_friend()
                            print "Total no of friends u have ryt now is %d"%(Total_friends)
                        elif (menu_choice == 3):
                            print "u entered send a secret msg block"
                            # this will give user the access to send a secret encrypted message
                            send_message()
                        elif (menu_choice == 4):
                            # this will give user the access to read a secret decrypted  message
                            print "u entered read a secret msg block"
                            read_message()
                        elif (menu_choice == 5):
                            print "u entered read chats from user block"
                            # this will give user the access to read the chat with older history
                            read_chat_history()
                        elif (menu_choice == 6):
                            #if user want to exit the application
                            Chat_flag=False
                        else:
                             print "invalid input"
                except Exception:
                    #exception is also used as it is a error prone area
                    print "value can only be integer"
