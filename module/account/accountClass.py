
from database import Database


class User(object):


        def __init__(self,_id,email,psw,icno,type):
                self._id=_id
                self.email=email
                self.psw=psw
                self.icno=icno
                self.type=type

        
        def save_to_mongodb(self):
            Database.insert(collection="users",data=self.json())    


        def json(self):  
                return {
                    "_id":self._id,
                    "email":self.email,
                    "psw":self.psw,
                    "icno":self.icno,
                    "type":self.type
                }
        
        @staticmethod
        def find_user(type,email):
               return Database.find_one(collection="users",query={'type':type,'email':email})
      
