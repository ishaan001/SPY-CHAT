from datetime import datetime
from colorama import Fore
import time

t=datetime.now()
print t.strftime("%A %d. %B %Y")
print t.strftime("%a, %d %b %Y %H:%M:%S +0000")
print Fore.MAGENTA+"hello"

#locat="Delhi"
#if __name__=='main':
 #   print "hello world"
  #  for i in range(10,20,2):
   #     print i
    #fibo=[]
    #a,b=0,1
    #while(b<1000):
     #   fibo.append(a)
      #  a,b=b,a+b
    #print fibo
i=["hello","MY",1,4.4,True]
print i
i.insert(2,23)
print i
z=i.count()
print z



