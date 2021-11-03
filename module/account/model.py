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
            #user_db=smartClassroom.users_db
            entry_email=form.email.data
            entry_psw=form.psw.data
            entry_ic=form.icno.data
            entry_type=request.form.get("selected-choice")
            entry_id=uuid.uuid4().hex
            #print(request.form)

            print(entry_email)

            #Encrypt the password
            entry_psw=pbkdf2_sha256.encrypt(entry_psw)

            #Passing the data to user class and retrive back store to "user" variable
            user=User(_id=entry_id,email=entry_email,psw=entry_psw,icno=entry_ic,type=entry_type)
            print(vars(user))
            user.save_to_mongodb()
            
            #user_db.insert_one(user)
            return redirect(url_for('login'))
        else:
            return render_template('account_module/registerPage.html',title='Register',form=form)

def login():
        form=loginForm()
        if request.method=="POST" and form.validate_on_submit:
            #user_db=smartClassroom.users_db
            entry_type=request.form.get("selected-choice")
            entry_email=form.email.data
            entry_psw=form.psw.data
        
            #print(entry_type)
            #print(entry_psw)
            #Passing the data to user class and retrive back store to "user" variable
            user=User.find_user(type=entry_type,email=entry_email)
 

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
      

       