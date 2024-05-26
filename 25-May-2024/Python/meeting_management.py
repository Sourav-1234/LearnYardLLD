from datetime import datetime,timedelta
from bisect import bisect_left,bisect_right

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email


class MeetingRoom:
    def __init__(self,name):
        self.name=name

class Meeting:
    def __init__(self,title,start_time,end_time,room,participants):
        self.title=title
        self.start_time=start_time
        self.end_time=end_time
        self.room=room
        self.participants=participants

class Scheduler:
    def __init__(self):
        self.meetings={}

    def schedule(self,meeting):
        if meeting.room not in self.meetings:
            self.meetings[meeting.room]=[]

        meetings=self.meetings[meeting.room]
        start_position= bisect_left(meetings,meeting,key=lambda x:x.start_time)
        end_position=bisect_right(meetings,meeting,key=lambda x:x.end_time)


        if(start_position<len(meetings) and meetings[start_position].start_time<meeting.end_time) or \
            (end_position>0 and meetings[end_position-1].end_time>meeting.start_time):
            raise Exception("Unavailble room !")

        meetings.insert(start_position,meeting)


class NotificationService:
    def send_notification(self,user,message):
        print(F"Sending Email to {user.email} :{message}")




user1=User("Sourav","sourav08saha@gmail.com")
user2=User("Sourav.s","sourav024saha@gmail.com")
room=MeetingRoom("Conference Room 1")
meeting=Meeting("Planning meeting" ,datetime.now(),datetime.now()+timedelta(hours=1),room,[user1,user2])
scheduler=Scheduler()
scheduler.schedule(meeting)

notification_service=NotificationService()
notification_service.send_notification(user1,"Your meeting has been scheduled ")
notification_service.send_notification(user2,"Your meeting has been scheduled ")