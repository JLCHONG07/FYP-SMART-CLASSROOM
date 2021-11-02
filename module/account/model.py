from flask import Flask,render_template,Response,request,redirect,url_for,flash
from wtforms.validators import ValidationError
import smartClassroom 
from passlib.hash import pbkdf2_sha256
import uuid
from appForm import loginForm,registerForm
from module.account.accountClass import User



def register():

        form=registerForm()
        if request.method=="POST":
            #get the MongoDB users table and get the email,password,icno,type,and id data from the form ("register.html")
            user_db=smartClassroom.users_db
            entry_email=form.email.data
            entry_psw=form.psw.data
            entry_ic=form.icno.data
            entry_type=request.form.get("selected-choice")
            entry_id=uuid.uuid4().hex
            #print(request.form)

            #Passing the data to user class and retrive back store to "user" variable
            user=User().user(_id=entry_id,email=entry_email,psw=entry_psw,icno=entry_ic,type=entry_type)
          
            # Encrypt the password
            user['psw']=pbkdf2_sha256.encrypt(user['psw'])

            user_db.insert_one(user)
            return redirect(url_for('login'))
        else:
            return render_template('account_module/registerPage.html',title='Register',form=form)

def login():
        form=loginForm()
        if request.method=="POST" and form.validate_on_submit:
            user_db=smartClassroom.users_db
            entry_type=request.form.get("selected-choice")
            entry_email=form.email.data
            entry_psw=form.psw.data
        
            #print(entry_type)
            #print(entry_psw)
            #Passing the data to user class and retrive back store to "user" variable
            user=User().user(_id=None,email=entry_email,psw=entry_psw,icno=None,type=entry_type)
            # data in side the user will be used to find the Mongodb database data and assign back to user after get the data
            user=user_db.find_one({ "type": user["type"], "email":user["email"],
               },{
                "_id":1,
                "email":1,
                "psw":1,
                "icno":1,
                "type":1,
            
            })
            
            #print(total_user)

            if user and pbkdf2_sha256.verify(entry_psw,user['psw']):
                 return redirect(url_for("mainMenu"))
                 
                
            else:
                #print if invalid user
                 error="Invalid email or password"
                 flash(error)
                 #return redirect(url_for("login"))
            return render_template('account_module/loginPage.html',title='Login',form=form)  
        else:
            return render_template('account_module/loginPage.html',title='Login',form=form)
      

       