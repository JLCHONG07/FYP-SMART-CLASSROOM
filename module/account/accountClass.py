
from flask.globals import session
from database import Database
from passlib.hash import pbkdf2_sha256

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
                
                if exists_user is not None:
                        return cls(**exists_user)

        @classmethod
        def get_user_email(cls,email):
                data=Database.find_one(collection="users",query={'email':email})
                if data is not None:
                        return cls(**data)                    
        
        @classmethod
        def get_user_icno(cls,icno):
                data=Database.find_one(collection="users",query={'icno':icno})
                if data is not None:
                        return cls(**data)                     

        @classmethod 
        def get_user_type(cls,type):
                data=Database.find_one(collection="users",query={'type':type})
                if data is not None:
                        return cls(**data) 

        @staticmethod
        def login_valid(email,psw,type):
                #('student1@gmail.com','123456','student')
                valid_user=User.find_user(type,email)

                if valid_user is not None and pbkdf2_sha256.verify(psw,valid_user.psw):
                        #passing useful information in Session
                        User.login(valid_user.email,valid_user.type)
                        return True
                else:
                        return False
        @staticmethod
        def login(user_email,user_type):
                session['email']=user_email
                session['type']=user_type

        @staticmethod
        def logout():
                session['email']=None
                session['type']=None

        @classmethod
        #Check the email is that alrdy exists and store it if not exists
        def register_valid(cls,id,email,psw,icno,type):
                user=User.get_user_email(email)

                if user is None:    
                        new_user=cls(id,email,psw,icno,type)
                        new_user.save_to_mongodb()
                        return True
                else:
                        return False

      
