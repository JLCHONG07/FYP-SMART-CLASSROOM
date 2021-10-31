from flask import Flask,render_template,Response
from hand_detection_and_recognation.hand_detection import hand_detection,hand_detection_mode_2


app=Flask(__name__)

@app.route("/")
def home():
    return render_template('homePage.html',title='Home')

@app.route("/login")
def login():
    return render_template('account_module/loginPage.html',title='Login')


@app.route("/register")
def register():
    return render_template('account_module/registerPage.html',title='Register')

@app.route("/mainMenu")
def mainMenu():
    return render_template('mainmenu.html',title='Main Menu')

@app.route("/mainMenu/smartQuiz")
def smartQuiz():
    return render_template('quizRoom.html',title='Smart Quiz')


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
   return Response(hand_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

def handRealtime2():
    return Response(hand_detection_mode_2(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__=='__main__':
    app.run(debug=True) 
