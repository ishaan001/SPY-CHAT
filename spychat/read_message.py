# this file will decrypt the message from resultant image

from select_friend import select_friend
# in this it used for decryption process
from steganography.steganography import Steganography
from default_spy_details import friends,ChatMessage
from datetime import datetime
import re

# colorama is used for colour coding
from colorama import Fore,Back,Style
def read_message():
    while(True):
        try:
            sender=select_friend()
            # decryption process
            while(True):
                decrpyt_it = raw_input("enter the file name\n")

                # regex pattern is user so that user can add oly images with .jpg and .JPG
                pattern_d = '[\w]+\.jpg|\.JPG+$'
                if (re.match(pattern_d,decrpyt_it)!= None):
                    break
                else:
                    print "please provide image with jpg format"
            secret_text = Steganography.decode(decrpyt_it)
            print Fore.MAGENTA+"message is %s"%secret_text
            word_speak = secret_text.split()
            friends[sender].count =+ len(word_speak)
        except Exception:
            print "Image doesn't contain any text"


        # average words spoken by your friend
        print "Average words said by : ",
        print (friends[sender].name),
        print " is ",
        print (friends[sender].count)

        if(len(word_speak)>100):
            print Fore.CYAN+friends[sender].name,
            print Fore.RED+"speaks too much ! HENCE HE's removed form your friend list "+Fore.RESET
            friends.remove(friends[sender])
        else:
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print (Fore.BLUE + "your secret message has been saved" + Fore.RESET)

        special = (secret_text.upper()).split()
        if "MAYDAY" in special or "SAVE" in special or "HELP" in special or "SOS" in special:
            # Emergency alert
            # help friend by sending a helping message
            print Fore.RED+"The friend who sent this message need your help.",
            print Fore.RED+"Select  friend to send helping message\n"

            friends_choice = select_friend()

            # send the helping text message to the friend in emergency.
            reply = "Help is on its way"

            # the message will be added to chat message class
            new_chat = ChatMessage(reply, True)

            # adding the message to friend in emergency
            friends[friends_choice].chats.append(new_chat)

            # the message has been sent successfully
            print Fore.GREEN+"You just sent a message to help your friend."+Fore.RESET
        break


