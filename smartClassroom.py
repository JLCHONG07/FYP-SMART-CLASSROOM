from flask import Flask
from hand_detection_and_recognation import class_calling


app=Flask(__name__)

app.add_url_rule('/','homePage',class_calling.getStart)
app.add_url_rule('/loginPage','login',class_calling.login)
app.add_url_rule('/registerPage','register',class_calling.register)

app.add_url_rule('/mainMenu','mainMenu',class_calling.mainMenu)
app.add_url_rule('/mainMenu/smartQuiz','smartQuiz',class_calling.smartQuiz)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu','quizMenu',class_calling.quizMenu)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz','quizRoom',class_calling.smartQuiz)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu','quizmenu',class_calling.quizMenu)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu','quizmenu',class_calling.quizMenu)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu/questionSummary','questionSummary',class_calling.questionSummary)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu/questionSummary/createQuizQuestion','createQuizQuestion',class_calling.createQuizQuestion)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu/answering','answering',class_calling.answering)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu/answering/handRealTimeCam','handRealTimeCam',class_calling.handRealtime)
app.add_url_rule('/mainMenu/smartQuiz/quizmenu/smartQuiz/quizMenu/reportSummary','reportSummary',class_calling.reportSummary)



if __name__=='__main__':
    app.run(debug=True) 
