#importing all the features of the application which are in different files
from read_chat_history import read_chat_history
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
def start_chat(name,age,rating,status):
        from globals import current_status_message
        if not (age >12 and age <50):
            print "Authentication failed Please Try again Later"
        else:
            Chat_flag=True
            while(Chat_flag):
                try:
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
                            current_status_message=add_status(current_status_message)
                        elif(menu_choice == 2):
                            print "u entered add a friend block"
                            Total_friends=add_friend()
                            print "Total no of friends u have ryt now is %d"%(Total_friends)
                        elif (menu_choice == 3):
                            print "u entered send a secret msg block"
                            send_message()
                        elif (menu_choice == 4):
                            print "u entered read a secret msg block"
                            read_message()
                        elif (menu_choice == 5):
                            print "u entered read chats from user block"
                            read_chat_history()
                        elif (menu_choice == 6):
                            Chat_flag=False
                        else:
                             print "invalid input"
                except Exception:
                    print "value can only be integer"
