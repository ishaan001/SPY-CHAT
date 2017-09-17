from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from default_spy_details import friends,ChatMessage
import re
def send_message():
    friend_choice=select_friend()
    while(True):
        original_img=raw_input("enter the name of the image where you want to hide the message\n")
        pattern_i='[\w]+\.jpg|\.JPG+$'
        if(re.match(pattern_i,original_img)!=None):
            break
        else:
            print "please provide image with jpg format"
    while(True):
        result_img=raw_input("Eneter the name of the resultant image\n")
        pattern_r='[\w]+\.jpg|\.JPG+$'
        if (re.match(pattern_r, result_img) != None):
            break
        else:
            print "please provide image with jpg format"

    encpyt_text=raw_input("enter the message which u want to encrypt\n")

    #encryption process
    Steganography.encode(original_img,result_img,encpyt_text)

    new_chat = ChatMessage(encpyt_text, True)
    friends[friend_choice].chats.append(new_chat)
    t=datetime.now();
    print "message sent successfully at "+str(t.strftime("%A %d. %B %Y"))