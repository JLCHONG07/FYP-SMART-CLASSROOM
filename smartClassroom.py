from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
from database import Database
from hand_detection_and_recognation.fingerCount import rmStartMode2
from hand_detection_and_recognation.hand_detection import hand_detection,hand_detection_mode_2
from pymongo import MongoClient
from module.account.accountClass import User
import module.account.model
import module.quizroom.quizroomModel
import module.answering.hand_detect_mode
import module.questions.questionsModel
import module.answering.answeringModel
import module.ranking_report.reportModel


app=Flask(__name__)
#client=MongoClient("mongodb+srv://fypsmartclassroom:fypsmartclassroom@fypsmartclassroom.t8u8i.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
#smartclassroom_db=client["smartclassroom"]
#users_db=smartclassroom_db["users"]

app.secret_key = "abc"  

@app.before_first_request
def database_initialize():
    Database.initialize()

@app.route("/")
@app.route("/homePage")
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

@app.route("/profile")
def profile():
    if session["email"] is not None:
        user=session["email"]
        print(user)
        return module.account.model.profile()
    else:
        return redirect(url_for('login'))

@app.route("/mainMenu/smartQuiz",methods=["GET","POST"])
def smartQuiz():
    if session['type'] == "admin":
        return module.quizroom.quizroomModel.quizrooms()
    else:
        studentSmartQuiz()
        
@app.route("/mainMenu/studentSmartQuiz",methods=["GET","POST"])
def studentSmartQuiz():
    return module.quizroom.quizroomModel.student_quizrooms()


#@app.route("/mainMenu/smartQuiz/editQuizRoom",methods=["GET","POST"])
#def editQuizRoom():
 #   editCreated=True
  #  return module.quizroom.quizroomModel.quizrooms(editCreated)
  #  */

@app.route("/mainMenu/smartQuiz/quizMenu")
@app.route("/mainMenu/studentSmartQuiz/quizMenu")
def quizMenu():
    return render_template('quizmenu.html',title='Quiz Menu')


@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction/")
def instruction():
    return module.answering.hand_detect_mode.instruction()

@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction/answering",methods=["GET","POST"])
def answering():
    return module.answering.answeringModel.answering()
    

@app.route("/mainMenu/smartQuiz/quizMenu/questionSummary",methods=["GET","POST"])    
def questionSummary():
    return module.questions.questionsModel.questionSummary()

@app.route("/mainMenu/smartQuiz/quizMenu/questionSummary/createQuetion",methods=["GET","POST"])
def createQuizQuestion():
     return module.questions.questionsModel.createQuestion()

@app.route("/mainMenu/smartQuiz/quizMenu/reportSummary/")
def reportSummary():
   return module.ranking_report.reportModel.reportSummary()

@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction/handRealTime")
def handRealtime():
    #session['hand-detect-mode']=1
    return Response(hand_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction/handRealTimeAndRecognize",methods=["GET","POST"])
def handRealTimeAndRecognize():
    #session['hand-detect-mode']=1
    return Response(rmStartMode2(), mimetype='multipart/x-mixed-replace; boundary=frame')



#@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction2/handRealTime2")
#def handRealtime2():
 #   session['hand-detect-mode']=2
 #   #instruction()
 #   return Response(hand_detection_mode_2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/logout")
@app.route("/mainMenu/logout")
@app.route("/mainMenu/smartQuiz/quizMenu/logout")
@app.route("/mainMenu/studentSmartQuiz/quizMenu/instruction/logout")
def logout():
    User.logout()
    return redirect(url_for('login'))

#@app.route("/mainMenu/joinQuizroom")
#def join_quizroom():
#   return module.quizroom.quizroomModel.join_quiz_room()

@app.route("/mainMenu/create_quizroom")
def create_quizroom():
   return module.quizroom.quizroomModel.create_quizroom()





if __name__=='__main__':
    app.run(debug=True) 
