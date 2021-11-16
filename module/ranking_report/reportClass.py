from database import Database
import uuid

class Report(object):

    def __init__(self,_id,quizroom_id,user_answered_details):
        self._id=_id if _id is None else _id
        self.quizroom_id=quizroom_id
        self.user_answered_details=user_answered_details
   

    def save_to_mongodb(self):
        Database.insert(query="report",data=self.json())

    
    def json(self):
        return{
            "_id":self._id,
            "quizroom_id":self.quizroom_id,
            "user_answered_details":self.user_answered_details

        }


    @classmethod
    def save_report(_cls,_id,quizroom_id,user_answered_details):
        Report.save_to_mongodb(_id,quizroom_id,user_answered_details)
