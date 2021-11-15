from types import coroutine
import uuid

from werkzeug.datastructures import MultiDict
from database import Database

class Answer(object):
    
    def __init__(self,answer_set,quizroom_id,_id):  
        self.quizroom_id=quizroom_id
        self.answer_set = answer_set
        self._id =uuid.uuid4().hex if _id is None else _id


    def save_to_mongodb(self):
        Database.insert(collection="answers",data=self.json())


    def update_to_mongodb(self):
        #print("update")
        Database.update(collection="answers",query={"quizroom_id":self.quizroom_id},update={"$push":{
              "answer_set":{
                "_id":self.answer_set[0],
                "curr_ques":self.answer_set[1],
                "curr_ques_ans":self.answer_set[2],
                "selected_answer":self.answer_set[3],
            }
        }},upsert=False,multi=True)
    
    def json(self):
        return {
            "quizroom_id":self.quizroom_id,
            "answer_set":[{
                "_id":self.answer_set[0],
                "curr_ques":self.answer_set[1],
                "curr_ques_ans":self.answer_set[2],
                "selected_answer":self.answer_set[3]
            }]
        }

    @classmethod
    def get_answer(cls,quizroom_id):
        data=Database.find_one(collection="answers",query={"quizroom_id":quizroom_id})
        #print(data)
        if data is not None:
            #print(cls(**data))
            return cls(**data)

    @staticmethod
    def get_all_answers(quizroom_id):
        return Database.find_one(collection="answers",query={"quizroom_id":quizroom_id})

    @staticmethod
    def display_all_answers(quizroom_id):
         #print("display all question _id:",quizroom_id)
         answer_exists=Answer.get_answer(quizroom_id)
         #print(question_exists)
         if question_exists is not None:
             return Answer.get_all_answers(quizroom_id)
