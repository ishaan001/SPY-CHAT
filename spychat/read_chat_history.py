#this file have been made to read the chat

from select_friend import select_friend
from default_spy_details import friends
from datetime import datetime
#colorama is used for colour coding
from colorama import init,Fore,Back
def read_chat_history():
    init()
    read_for=select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            #init() method is used to initialize the object of module COLORAMA
            init()
            print Fore.BLUE+'[%s]'%chat.time.strftime("%d %B %Y")
            print Fore.RED+'%s' %('You said')
            print Fore.CYAN+'%s'%chat.message
            print Fore.RESET

        else:
            init()
            print Fore.BLACK+'[%s]'%chat.time.strftime("%d %B %Y")
            print Fore.RED+'%s said:'%friends[read_for].name
            print Fore.CYAN+'%s'%chat.message
    print Fore.RESET

