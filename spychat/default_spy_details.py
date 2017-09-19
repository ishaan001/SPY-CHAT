from datetime import datetime
#Default spy details concept of classes is also used
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None
    self.count=0

spy = Spy('Ishaan', 'Mr', 20, 5.0)

friend_one = Spy('Raja', 'Mr', 27, 4.9)
friend_two = Spy('rani', 'Ms', 21, 4.39)
friend_three = Spy('Barati', 'Dr', 37, 4.95)

friends = [friend_one, friend_two, friend_three]

#class ChatMessage is used to get the message sent by the user to his/her friends
class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me