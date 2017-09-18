class Person:
    FirstName=''
    MiddleName=''
    LastName=''
    counter = 0
    def GetConName(self):
        return self.FirstName+' '+self.MiddleName+' '+self.LastName
    def __init__(self):
        print "bakloli"
        Person.counter +=1
        print Person.counter

Ishaan=Person()
Ishaan.FirstName='ishaan'
Ishaan.MiddleName='veer'
Ishaan.LastName='dadhwal'
print Ishaan.GetConName()
shekhar =Person()




spy={
    "name":"ishaan",
    "salutation":"Mr",
    "age":20,
    "rating":5.0,
    "status":False
}


'''   new_friend={
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'status':False,
        'chats':[]
    }'''

friends = []


