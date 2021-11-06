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
    def find(collection,query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,query,update):
        return Database.DATABASE[collection].update(query,update)

    #@staticmethod
    ##def aggregate_count(collection,query):
    #    return Database.DATABASE[collection].aggregate([{"$count":"quizrooms.quiz_code"}])

    
    #@staticmethod
    #def my_update_one_test():
    #    return Database.DATABASE['quizrooms'].update({"belongs_to":"student2@gmail.com","quizrooms._id":"2ba74ded8fcd446da652c7574ca51b4a"},{"$set":{"quizrooms.$.subject":"Science" }})
    
    @staticmethod
    def find_total(collection,query):
        return Database.DATABASE[collection].find({},query)

