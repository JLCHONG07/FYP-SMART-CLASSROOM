from database import Database
import uuid

class Report(object):

    def __init__(self,quizroom_id,user_answered_details,_id):
        self._id=uuid.uuid4().hex if _id is None else _id
        self.quizroom_id=quizroom_id
        self.user_answered_details=user_answered_details
   

    def save_to_mongodb(self):
        Database.insert(collection="reports",data=self.json())

    def update_to_mongodb(self):
        #print("update")
        Database.update(collection="reports",query={"quizroom_id":self.quizroom_id},update={"$push":
        {
                "user_answered_details":{
                "email":self.user_answered_details[0],
                "points":self.user_answered_details[1],
            
            }
        }},upsert=False,multi=True)

    def json(self):
        return{
            "_id":self._id,
            "quizroom_id":self.quizroom_id,
            "user_answered_details":[{
                "email":self.user_answered_details[0],
                "points":self.user_answered_details[1]
            }]

        }


    @classmethod
    def save_report(cls,quizroom_id,user_answered_details,_id):

        report_exists=Report.report_exists(quizroom_id)
        if report_exists is None:
                saving_report=cls(quizroom_id,user_answered_details,_id)
                saving_report.save_to_mongodb()
        else:
                update_report=cls(quizroom_id,user_answered_details,_id)
                update_report.update_to_mongodb()


    @staticmethod
    def report_exists(quizroom_id):
        data=Database.find_one(collection="reports",query={"quizroom_id":quizroom_id})

        if data is not None:
            return data


