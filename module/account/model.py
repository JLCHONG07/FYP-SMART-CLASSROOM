
from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
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
            #print(entry_email)
            #Encrypt the password
            entry_psw=pbkdf2_sha256.encrypt(entry_psw)

            #user=User.get_user_email(entry_email)
            #print(vars(user))
            #Passing the data to user class and retrive back store to "user" variable
            #user=User(_id=entry_id,email=entry_email,psw=entry_psw,icno=entry_ic,type=entry_type)

            #Check the email is that alrdy exists and store it if not exists
            if User.register_valid(entry_id,entry_email,entry_psw,entry_ic,entry_type):
                session.pop('_flashes', None)
                return redirect(url_for('login'))
            else:
                flash("Email already exists")
            return render_template('account_module/registerPage.html',title='Register',form=form)
            #print(vars(user))
            #user.save_to_mongodb()
            
            #user_db.insert_one(user)
            #return redirect(url_for('login'))
            #return render_template('account_module/registerPage.html',title='Register',form=form)
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
            #user=User.find_user(type=entry_type,email=entry_email)
            #print(vars(user))

            #Check if user email,password is valid with type selected
            if User.login_valid(entry_email,entry_psw,entry_type):
                 #flash("Account Created")
                 return redirect(url_for("mainMenu"))
        
            else:
                #print if invalid user
                 error="Invalid email or password"
                 flash(error)
                 User.logout()
                 #return redirect(url_for("login"))
            return render_template('account_module/loginPage.html',title='Login',form=form)  
        else:
            return render_template('account_module/loginPage.html',title='Login',form=form)

def profile():

    type=session['type']
    email=session['email']
    print("type",type)
    print("email",email)
    user_details=User.find_user(type,email)
    return render_template('profile.html',title="Profile",user=user_details)

      

       