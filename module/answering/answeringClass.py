from types import coroutine
import uuid

from werkzeug.datastructures import MultiDict
from database import Database

class Answer(object):
    
    _answered=0
    def __init__(self,quizroom_id,email,points,progress,answered_set,_id):  
        self.quizroom_id=quizroom_id
        self.email=email
        self.points=points
        self.answered_set=answered_set
        self.progress=progress
        self._id=uuid.uuid4().hex if _id is None else _id


    def save_to_mongodb(self):
        Database.insert(collection="answers",data=self.json())


    def update_to_mongodb(self):
        #print("update")
        Database.update(collection="answers",query={"quizroom_id":self.quizroom_id,"email":self.email},update={"$push":
        {
                "answered_set":{
                "question_id":self.answered_set[0],
                "selected_answer":self.answered_set[1],
                "correct_answer":self.answered_set[2],
                "remark":self.answered_set[3]
            }
        }},upsert=False,multi=True)

    def update_point_to_mongodb(self):
        #print("update")
        Database.update(collection="answers",query={"quizroom_id":self.quizroom_id,"email":self.email},update={"$set":
        {
               "points":self.points
        }},upsert=False,multi=True)  

  
    def json(self):
        return {
            "_id":self._id,
            "quizroom_id":self.quizroom_id,
            "email":self.email,
            "points":self.points,
            "progress":self.progress,
            "answered_set":[{
                "question_id":self.answered_set[0],
                "selected_answer":self.answered_set[1],
                "correct_answer":self.answered_set[2],
                "remark":self.answered_set[3]
            }]
        }

    @classmethod
    def get_answer(cls,email,quizroom_id):
        data=Database.find_one(collection="answers",query={"email":email,"quizroom_id":quizroom_id})
        #print(data)
        if data is not None:
            #print(cls(**data))
            return cls(**data)

    @staticmethod
    def get_all_answers(email):
        return Database.find_one(collection="answers",query={"email":email})

    @staticmethod
    def get_answered_question(quizroom_id,question_id,email):
        data= Database.find(collection="answers",query={"email":email,"quizroom_id":quizroom_id},
        data={"_id":0,"quizroom_id":0,"email":0,"points":0,"progress":0,"answered_set":{"$elemMatch":{"question_id":question_id}}})
        #check the list len if the list length for question_id is empty mean it dones no has any length
        
        question_id_exists=None
        for x in data:
            print("question_id_exists",x)
            question_id_exists=len(x)
        if question_id_exists==0:
            return True
        else:
            return False

    #@staticmethod
    #def display_all_answers(quizroom_id):
         #print("display all question _id:",quizroom_id)
        # answer_exists=Answer.get_answer(quizroom_id)
         #print(question_exists)
         #if answer_exists is not None:
             #return Answer.get_all_answers(quizroom_id)


    @classmethod
    def save_with_check(cls,quizroom_id,email,points,progress,answered_set,_id):
        #check is that new answer for this user?
        #convert selected answer from 1,2,3,4 to a1,a2,a3,a4
        #compare is that selected answer == correct answer
        #assign remark to "true" if the answer is correct, else to "false"
        #if it is new user, save_to_mongodb
        #else update_to_mongodb
        new_answer=Answer.get_answer(email,quizroom_id)
        selected_answer=Answer.reassign_answer(answered_set[1])
        #print("selected_answer",selected_answer)
        check_answer,points=Answer.check_answer(selected_answer,answered_set[2],points)
        answered_set[3]=Answer.checked_answer(check_answer)
        if new_answer is None:
            new_answer=cls(quizroom_id,email,points,progress,answered_set,_id)
            new_answer.save_to_mongodb()
        else:
            check_question_id_exists=Answer.get_answered_question(quizroom_id,answered_set[0],email)
            #only points will update and keep the first answer
            if check_question_id_exists:
                print("save None")
                update_answered=cls(quizroom_id,email,points,progress,answered_set,_id)
                update_answered.update_to_mongodb()
                update_answered=cls(quizroom_id,email,points,progress,answered_set,_id)
                update_answered.update_point_to_mongodb()
            else:
                print("save not None")
                update_answered=cls(quizroom_id,email,points,progress,answered_set,_id)
                update_answered.update_point_to_mongodb()


    @staticmethod
    def complete_update(quizroom_id,email,progress):
         Database.update(collection="answers",query={"quizroom_id":quizroom_id,"email":email},update={"$set":
        {
               "progress":progress
        }},upsert=False,multi=True) 
    


            
    @staticmethod
    def reassign_answer(selected_answer):
        convert_result=None
        if selected_answer == "1":
            convert_result="a1"
        elif selected_answer == "2":
            convert_result="a2"
        elif selected_answer == "3":
            convert_result="a3"
        elif selected_answer == "4":
            convert_result="a4"

        return convert_result

    @staticmethod
    def check_answer(selected_answer,correct_answer,points):
        result=False

        if selected_answer == correct_answer:
            result=True
            points+=10

        return result,points

    @staticmethod
    def checked_answer(check_answer):

        if check_answer:
            return "true"
        else:
            return "false"

    @staticmethod
    def get_answered_details(quizroom_id,email):
        data=Database.find(collection="answers",query={"quizroom_id":quizroom_id,"email":email},data={"points":1,"answered_set":1})
        return data
    

    @staticmethod
    def new_answer_user(email,quizroom_id,progress):
        new_users=Answer.get_answer(email,quizroom_id)
        print('new users',new_users.progress)
        
        if new_users.progress == "pending":
            Answer.complete_update(quizroom_id,email,progress)
            return True
        else:
            return False
    