# this file will encrypt the message into resultant image provided by user
from select_friend import select_friend
# steganography is used  to encrypt the data inside the image

from steganography.steganography import Steganography

# datetime module is used to get the date and time
from datetime import datetime

from default_spy_details import friends,ChatMessage

# re module is used to add regex pattern
import re

# colorama is used for colour coding
from colorama import Fore,init
def send_message():
    friend_choice=select_friend()
    while(True):
        original_img=raw_input("enter the name of the image where you want to hide the message and image should be of JPG TYPE\n")

        #regex pattern is user so that user can add oly images with .jpg and .JPG
        pattern_i='[\w]+\.jpg|\.JPG+$'
        if(re.match(pattern_i,original_img)!=None):
            break
        else:
            print "please provide image with jpg format"
    while(True):
        result_img=raw_input("Eneter the name of the resultant image and image should be of JPG TYPE\n")

        # regex pattern is user so that user can add oly images with .jpg and .JPG
        pattern_r='[\w]+\.jpg|\.JPG+$'
        if (re.match(pattern_r, result_img) != None):
            break
        else:
            print "please provide image with jpg format"

    encpyt_text=raw_input("enter the message which u want to encrypt")
    if(len(encpyt_text)!=0):
        Steganography.encode(original_img,result_img,encpyt_text)
        new_chat = ChatMessage(encpyt_text, True)
        friends[friend_choice].chats.append(new_chat)
        t = datetime.now()
        init()
        print Fore.CYAN+"message sent successfully at ",
        print str(t.strftime("%A %d. %B %Y"))
        print Fore.RESET

    else:
        init()
        print Fore.CYAN+'image do no contain any text please provide so!! BYE :D'+Fore.RESET


