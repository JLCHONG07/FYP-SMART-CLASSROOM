
class User:

    def user(self,_id,email,psw,icno,type):  
            user={
                    "_id":_id,
                    "email":email,
                    "psw":psw,
                    "icno":icno,
                    "type":type

            }
            return user
