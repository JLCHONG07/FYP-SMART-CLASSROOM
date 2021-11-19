import uuid
from database import Database

class Question(object):
    
    def __init__(self,quizroom_id,question_set,_id):
        self.quizroom_id=quizroom_id
        self.question_set=question_set
        self._id=uuid.uuid4().hex if _id is None else _id
    
    def save_to_mongodb(self):
        Database.insert(collection="questions",data=self.json())

    def update_to_mongodb(self):
        #print("update")
        Database.update(collection="questions",query={"quizroom_id":self.quizroom_id},update={"$push":{
              "question_set":{
                "_id":self.question_set[0],
                "question":self.question_set[1],
                "answer1":self.question_set[2],
                "answer2":self.question_set[3],
                "answer3":self.question_set[4],
                "answer4":self.question_set[5],
                "correct_answer":self.question_set[6]
            }
        }},upsert=False,multi=True)
    
    def json(self):
        return {
            "quizroom_id":self.quizroom_id,
            "question_set":[{
                "_id":self.question_set[0],
                "question":self.question_set[1],
                "answer1":self.question_set[2],
                "answer2":self.question_set[3],
                "answer3":self.question_set[4],
                "answer4":self.question_set[5],
                "correct_answer":self.question_set[6]
            }]
        }

    @classmethod
    def get_question(cls,quizroom_id):
        data=Database.find_one(collection="questions",query={"quizroom_id":quizroom_id})
        #print(data)
        if data is not None:
            #print(cls(**data))
            return cls(**data)

    @staticmethod
    #This will get all the question_id
    def get_question_with_question_id(question_id):
        data= Database.find(collection="questions",query={"question_set._id":question_id}
        ,data={"_id":0,"quizroom_id":0,"question_set":{"$elemMatch":{"_id":question_id}}})
        #print(vars(data))
        #for x in data:
            #print("my x")
            #print(x)
        if data is not None:
            return data

    @staticmethod
    def get_all_questions(quizroom_id):
        return Database.find_one(collection="questions",query={"quizroom_id":quizroom_id})

    @classmethod
    def get_created_question(cls,quizroom_id,question_set,_id):
        question_exists=Question.get_question(quizroom_id)

        if question_exists is None:
            create_question=cls(quizroom_id,question_set,_id)
            create_question.save_to_mongodb()
        else:
            print("exists questions")
            add_question=cls(quizroom_id,question_set,_id)
            add_question.update_to_mongodb()

    @staticmethod
    def display_all_question(quizroom_id):
         #print("display all question _id:",quizroom_id)
         question_exists=Question.get_question(quizroom_id)
         #print(question_exists)
         if question_exists is not None:
             return Question.get_all_questions(quizroom_id)

    @staticmethod
    def search_question_id(question_id):
        exists_question=Question.get_question_with_question_id(question_id)
        if exists_question is not None:
            return exists_question

    #edit question
    @staticmethod
    def edit_question(question_id,question,answer1,answer2,answer3,answer4,correct_ans):
        exists_question=Question.get_question_with_question_id(question_id)
        if exists_question is not None:
            #print(question_id,question,answer1,answer2,answer3,answer4,correct_ans)
            data=Database.update(collection="questions",query={"question_set._id":question_id},
            update={"$set":
            {"question_set.$.question":question,
            "question_set.$.answer1":answer1,
            "question_set.$.answer2":answer2,
            "question_set.$.answer3":answer3,
            "question_set.$.answer4":answer4,
            "question_set.$.correct_answer":correct_ans,
            }},upsert=False,multi=True)
            if data is not None:
                return True
            else:
                return False
    
    @staticmethod
    #Removing the question
    def delete_question(question_id):
        exists_question=Question.get_question_with_question_id(question_id)
        if exists_question is not None:
            data=Database.update(collection="questions",query={"question_set._id":question_id},
            update={"$pull":{"question_set":{"_id":question_id}}},upsert=False,multi=True)
            #print(data)
            if data is not None:
                return True
            else:
                return False


