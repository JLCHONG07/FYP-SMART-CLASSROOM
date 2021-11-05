import uuid
from flask.globals import session
from database import Database




class Quizroom:

    def __init__(self,subject,total_progress,assigned_to,quiz_code,belongs_to,_id=None):
       
     
        self.subject=subject
        self.total_progress=total_progress
        self.assigned_to=assigned_to
        self.quiz_code=quiz_code
        self.belongs_to=belongs_to
        #self.classroom=[]
        self._id=uuid.uuid4().hex if _id is None else _id
        
 
    
    def save_to_mongodb(self):
        Database.insert(collection="quizrooms",data=self.json())


    def update_to_mongodb(self):
        query="{"+"belongs_to :"+self.belongs_to+"}"
        print(query)
        update=self.json_update()
        print(update)
        Database.update(collection="quizrooms",query={"belongs_to":self.belongs_to},update={"$push":{
                "quizrooms":{
                "subject":"subject2",
                "total_progress":23,
                "assigned_to":"Group 3",
                "quiz_code":787878,
                "_id":"4567890"
                }
             }})
        

    def json(self):  

        return {
            
            "belongs_to":self.belongs_to,
            "quizrooms":[{
               "subject":self.subject,
              "total_progress":self.total_progress,
             "assigned_to":self.assigned_to,
             "quiz_code":self.quiz_code,
             "_id":self._id,
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
    

    @staticmethod
    def get_quizroom(email):
        quizrooms=Database.find_one(collection="quizrooms",query={'belongs_to':email})
        #print(classrooms)
        if quizrooms is not None:
            return quizrooms
                      
            

    #@classmethod
    #def get_subject(cls,subject):
     #   return

    #@classmethod
    #def get_total_progress(cls,total_progress):
     #   return

    #@classmethod
    #def get_assigned_to(self,total_progress):
    #    return

    #@classmethod
    #def get_class_code(cls,class_code):
    #   return

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
    def create_new_quizroom(cls,subject,total_progress,assigned_to,quiz_code,belongs_to,_id):
        #new_classroom=Classroom.get_classroom(email)
        update_to_exsists=cls.quizroom_exists(belongs_to)

        if update_to_exsists:
            update_quizroom=cls(subject,total_progress,assigned_to,quiz_code,belongs_to,_id)
            update_quizroom.update_to_mongodb()
        else:
            new_quizroom=cls(subject,total_progress,assigned_to,quiz_code,belongs_to,_id)
            new_quizroom.save_to_mongodb()
            

