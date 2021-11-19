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

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,query,update,upsert,multi):
        return Database.DATABASE[collection].update(query,update,upsert,multi)

    @staticmethod
    def find_total(collection,query):
        return Database.DATABASE[collection].find({},query)

    @staticmethod
    def distinct(collection,value,query):
        return Database.DATABASE[collection].distinct(value,query)
