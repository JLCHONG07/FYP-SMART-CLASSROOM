from typing import Collection
import pymongo


class Database(object):

    URI="mongodb+srv://fypsmartclassroom:fypsmartclassroom@fypsmartclassroom.t8u8i.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE"
    DATABASE=None

    @staticmethod
    def initialize():
        client=pymongo.MongoClient(Database.URI)
        Database.DATABASE=client["smartclassroom"]
    
    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection,query,data):
        return Database.DATABASE[collection].find(query,data)
        #return Database.DATABASE["quizrooms"].find({"quizrooms.quiz_code":208660},{"_id":1,"belongs_to":1,"quizrooms._id":1})

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,query,update,upsert,multi):
        return Database.DATABASE[collection].update(query,update,upsert,multi)

    #@staticmethod
    ##def aggregate_count(collection,query):
    #    return Database.DATABASE[collection].aggregate([{"$count":"quizrooms.quiz_code"}])

    
    #@staticmethod
    #def my_update_one_test():
    #    return Database.DATABASE['quizrooms'].update({"belongs_to":"student2@gmail.com","quizrooms._id":"2ba74ded8fcd446da652c7574ca51b4a"},{"$set":{"quizrooms.$.subject":"Science" }})
    
    @staticmethod
    def find_total(collection,query):
        return Database.DATABASE[collection].find({},query)

    #@staticmethod
    #def distinct_value():
    #    return Database.DATABASE['quizrooms'].distinct("quizrooms._id",
    #    {"quizrooms":{"$elemMatch":{"quiz_code":208660}}})

    #NEW_OBJECT={
    #    "quizroom_id":"d1de51c394834b38959fb68c4686cbda"
    #}
    #@staticmethod
    #def update_detail():
    #    return Database.DATABASE['users'].update({"email":"student1@gmail.com"},
    #    {"$push":{"quizroom_joined":Database.NEW_OBJECT}})


    @staticmethod
    def distinct(collection,value,query):
        return Database.DATABASE[collection].distinct(value,query)

    #@staticmethod
    #def count_total():
     #   return Database.DATABASE["users"].find({"quizroom_joined.quizroom_id": "d1de51c394834b38959fb68c4686cbda"},
      #  {"quizrom_joined":{"$elemMatch":{"quizroom_id":"d1de51c394834b38959fb68c4686cbda"}}}).count()

    #@staticmethod
    ##def distinct_test():
    #    return Database.DATABASE['users'].distinct("quizroom_joined.quizroom_id",{"email":"student1@gmail.com"})
    

