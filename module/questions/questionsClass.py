import uuid
from database import Database

class Questions(object):
    
    def __init__(self,_id,quizroom_id,question_set):
        self._id=_id
        self.quizroom_id=quizroom_id
        self.question_set=question_set
        #self.question_no=question_no
        #self.question=question
        #self.answer1=answer1
        #self.answer2=answer2
        #self.answer3=answer3
        #self.answer4=answer4
        #self.correct_answer=correct_answer

    
    @classmethod
    def save_to_mongodb(self):
        Database.insert(collection="questions",data=self.json())

    @classmethod
    def json(self):
        return {
            "quizroom_id":self.quizroom_id,
            "question_set":{
                "_id":self.question_set[0],
                "question":self.question_set[1],
                "answer1":self.question_set[2],
                "answer2":self.question_set[3],
                "answer3":self.question_set[4],
                "answer4":self.question_set[5],
                "correct_answer":self.question_set[6]
            }
        }
