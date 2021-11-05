from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
from database import Database
from hand_detection_and_recognation.hand_detection import hand_detection,hand_detection_mode_2
from pymongo import MongoClient
from module.account.accountClass import User
import module.account.model
import module.quizroom.quizroomModel


app=Flask(__name__)
#client=MongoClient("mongodb+srv://fypsmartclassroom:fypsmartclassroom@fypsmartclassroom.t8u8i.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
#smartclassroom_db=client["smartclassroom"]
#users_db=smartclassroom_db["users"]

app.secret_key = "abc"  

@app.before_first_request
def database_initialize():
    Database.initialize()

@app.route("/")
def home():
    return render_template('homePage.html',title='Home')

@app.route("/login",methods=["GET","POST"])
def login():
  
    return module.account.model.login()


@app.route("/register",methods=["GET","POST"])
def register():
    return module.account.model.register()
  
@app.route("/mainMenu")
def mainMenu():
    if session["email"] is not None:
        user=session["email"]
        print(user)
        return render_template('mainmenu.html',title='Main Menu')
    else:
        return redirect(url_for('login'))

@app.route("/mainMenu/smartQuiz")
def smartQuiz():
    return module.quizroom.quizroomModel.quizrooms()


@app.route("/mainMenu/smartQuiz/quizMenu")
def quizMenu():
    return render_template('quizmenu.html',title='Quiz Menu')

@app.route("/mainMenu/smartQuiz/quizMenu/answering")
def answering():
    return render_template('answering.html',title='Answer')

@app.route("/mainMenu/smartQuiz/quizMenu/questionSummary")    
def questionSummary():
    return render_template('questionSummary.html',title='Question Summary')

@app.route("/mainMenu/smartQuiz/quizMenu/questionSummary/createQuetion")
def createQuizQuestion():
      
    return render_template('createQuestion.html',title='Create Quiz Question')

@app.route("/mainMenu/smartQuiz/quizMenu/reportSummary/")
def reportSummary():
    return render_template('reportSummary.html',title='Report Summary')

@app.route("/mainMenu/smartQuiz/quizMenu/answering/handRealTime")
def handRealtime():
   return Response(hand_detection(), mimetype='multipart/x-mixed-replace; boundary=frame',title="hand_detect_mode1")

def handRealtime2():
    return Response(hand_detection_mode_2(), mimetype='multipart/x-mixed-replace; boundary=frame',title="hand_detect_mode2")

@app.route("/logout")
def logout():
    User.logout()
    return redirect(url_for('login'))

@app.route("/mainMenu/create_quizroom")
def create_quizroom():
   return module.quizroom.quizroomModel.create_quizroom()

if __name__=='__main__':
    app.run(debug=True) 
