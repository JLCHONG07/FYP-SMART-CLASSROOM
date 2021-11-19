
from flask import render_template,request,redirect,url_for,flash
from flask.globals import session
from passlib.hash import pbkdf2_sha256
import uuid
from appForm import loginForm,registerForm
from module.account.accountClass import User



def register():

        form=registerForm()
        if request.method=="POST":
            #get the MongoDB users table and get the email,password,icno,type,and id data from the form ("register.html")
            entry_email=form.email.data
            entry_psw=form.psw.data
            entry_ic=form.icno.data
            entry_type=request.form.get("selected-choice")
            entry_id=uuid.uuid4().hex
            #print(request.form)
            #print(entry_email)
            entry_psw=pbkdf2_sha256.encrypt(entry_psw)

            #Check the email is that alrdy exists and store it if not exists
            if User.register_valid(entry_id,entry_email,entry_psw,entry_ic,entry_type):
                session.pop('_flashes', None)
                return redirect(url_for('login'))
            else:
                flash("Email already exists")
            return render_template('account_module/registerPage.html',title='Register',form=form)

        else:
            return render_template('account_module/registerPage.html',title='Register',form=form)

def login():
        form=loginForm()
        if request.method=="POST" and form.validate_on_submit:
            entry_type=request.form.get("selected-choice")
            entry_email=form.email.data
            entry_psw=form.psw.data
        
            #Check if user email,password is valid with type selected
            if User.login_valid(entry_email,entry_psw,entry_type):
                 return redirect(url_for("mainMenu"))
        
            else:
                 #print if invalid user
                 error="Invalid email or password"
                 flash(error)
                 User.logout()
            return render_template('account_module/loginPage.html',title='Login',form=form)  
        else:
            return render_template('account_module/loginPage.html',title='Login',form=form)

def profile():
    #display the user details in profile
    type=session['type']
    email=session['email']
    print("type",type)
    print("email",email)
    user_details=User.find_user(type,email)
    return render_template('profile.html',title="Profile",user=user_details)

      

       