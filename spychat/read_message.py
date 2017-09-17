from select_friend import select_friend
from steganography.steganography import Steganography
from default_spy_details import friends,ChatMessage
from datetime import datetime
import re
from colorama import Fore,Back,Style
def read_message():
    while(True):
        try:
            sender=select_friend()
            #decryption process
            while(True):
                decrpyt_it=raw_input("enter the file name\n")
                pattern_d = '[\w]+\.jpg|\.JPG+$'
                if (re.match(pattern_d,decrpyt_it)!= None):
                    break
                else:
                    print "please provide image with jpg format"
            secret_text=Steganography.decode(decrpyt_it)
        except Exception:
            print "Image not find"

        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)
        print (Fore.BLUE + "your secret message has been saved"+Fore.RESET)
        break


