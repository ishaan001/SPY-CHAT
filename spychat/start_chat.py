from add_status import add_status
def start_chat(name,age,rating):
    from globals import curremt_status_message
    if not (age >12 and age <50):
        print "Authentication failed Please Try again Later"
    else:
        Chat_flag=True
        while(Chat_flag):
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
                    curremt_status_message=add_status(curremt_status_message)
                elif(menu_choice == 2):
                    print "u entered add a friend block"
                elif (menu_choice == 3):
                    print "u entered send a secret msg block"
                elif (menu_choice == 4):
                    print "u entered read a secret msg block"
                elif (menu_choice == 5):
                    print "u entered read chats from user block"
                elif (menu_choice == 6):
                    Chat_flag=False
                else:
                    print "invalid input"

