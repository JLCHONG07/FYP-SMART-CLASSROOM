import uuid
from flask.globals import session
from database import Database
from random import randint



class Quizroom(object):

    def __init__(self,belongs_to,quizrooms,_id=None):
       
        self.belongs_to=belongs_to
        self.quizrooms=quizrooms
        self._id=uuid.uuid4().hex if _id is None else _id
        
 
    
    def save_to_mongodb(self):
        Database.insert(collection="quizrooms",data=self.json())


    def update_to_mongodb(self):
        query="{"+"belongs_to :"+self.belongs_to+"}"
        #print(query)
        update=self.json_update()
        #print(update)
        Database.update(collection="quizrooms",query={"belongs_to":self.belongs_to},update={"$push":{
                "quizrooms":{
                "subject":self.quizrooms[0],
                "total_progress":self.quizrooms[1],
                "assigned_to":self.quizrooms[2],
                "quiz_code":self.quizrooms[3],
                 "total_students":self.quizrooms[4],
                "_id":"4567890"
                }
             }})
        

    def json(self):  

        return {
            
            "belongs_to":self.belongs_to,
            "_id":self._id,
            "quizrooms":[{
               "subject":self.quizrooms[0],
              "total_progress":self.quizrooms[1],
             "assigned_to":self.quizrooms[2],
             "quiz_code":self.quizrooms[3],
             "total_students":self.quizrooms[4],
             "_id":self.quizrooms[5],
            }]

        }

    
    #not json_update using as there is some problem (TypeError: spec must be an instance of dict, bson.son.SON, or any other type that inherits from collections.Mapping Traceback (most recent call last))
    def json_update(self):
        return{
             "$push":{
                "quizrooms":{
                "subject":"subject2",
                "total_progress":23,
                "assigned_to":"Group 3",
                "quiz_code":787878,
                "_id":"4567890"
                }
             }
        }
    

    @classmethod
    def get_quizroom(cls,email):
        data=Database.find_one(collection="quizrooms",query={'belongs_to':email})
        #print(classrooms)
        if data is not None:
            return cls(**data)

    
    @staticmethod
    def quizroom_exists(email):

        quizroom_exists=Quizroom.get_quizroom(email)

        if quizroom_exists is not None:
           return True

        else:
            return False

    @staticmethod
    def display_all_quizrooms(email):
       return  Database.find_one(collection="quizrooms",query={'belongs_to':email})

    @classmethod
    def create_new_quizroom(cls,belongs_to,quizrooms,_id):
        #new_classroom=Classroom.get_classroom(email)
        update_to_exsists=cls.quizroom_exists(belongs_to)
        quizrooms[3]=Quizroom.create_new_quiz_code()
        print(quizrooms[3])

        if update_to_exsists:
            update_quizroom=cls(belongs_to,quizrooms,_id)
            update_quizroom.update_to_mongodb()
        else:
         
            new_quizroom=cls(belongs_to,quizrooms,_id)
            new_quizroom.save_to_mongodb()

    @staticmethod
    def create_new_quiz_code():
        #random a 6 digit number
        #check from database
        #if didnot has this numbers return the quiz_code, else random again to avoid duplication
        quiz_code_exists=False
        while not quiz_code_exists:
            quiz_code=Quizroom.random_quiz_code()
            quiz_code_exists=Quizroom.quiz_code_exists(quiz_code)

        return quiz_code

    #random 6 digit numbers
    @staticmethod
    def random_quiz_code():
        return randint(100000,999999)

    #check from database is that the code used
    @staticmethod
    def quiz_code_exists(quiz_code):
        data=Database.find_one(collection="quizrooms",query={"quizrooms.quiz_code":quiz_code})
        print(data)
        if data is None :
            return True
        else:
            return False
            

