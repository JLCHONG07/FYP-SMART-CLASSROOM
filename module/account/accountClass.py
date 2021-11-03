
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
        
        @classmethod
        def find_user(cls,type,email):
               exists_user=Database.find_one(collection="users",query={'type':type,'email':email})

               return cls(_id=exists_user['_id'],
                          email=exists_user['email'],
                          psw=exists_user['psw'],
                          icno=exists_user['icno'],
                          type=exists_user['type'])
      
