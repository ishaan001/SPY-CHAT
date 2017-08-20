'''name=raw_input("enter your name")
if len(name)>0:
    if(name==" "):
        print "u entered space instead of name"
    elif(name=="  "):
        print "u entered space instead of name"
    else:
        print "ur name is "+name+" thank u for being with us"
        init = raw_input("enter ur salutation")
        if(init=="Mr" or init=="Ms"):
            print "hello "+init+"."+name
        else:
            print "salutation not provided correctly"
else:
    print "u haven't entered any data try again"

#print ' hello 1 called'
#val="Ishaan"
#age=19.55
#print "%s %d is the president of lakshya"%(val,age)
#print age<0'''

list =['ishaan','is','a','good',10,11,12]
j=len(list);
for i in range(0,j):
    print str(i)+" "+str(list[i]);


