from flask import render_template, request, Response
import os
from hand_detection_and_recognation.hand_detection import hand_detection,hand_detection_mode_2


def getStart():
    return render_template('homePage.html',title='Home')

def login():
    return render_template('account_module/loginPage.html',title='Login')



def register():
    return render_template('account_module/registerPage.html',title='Register')


def mainMenu():
    return render_template('mainmenu.html',title='Main Menu')

def smartQuiz():
    return render_template('quizRoom.html',title='Smart Quiz')


def answering():
    return render_template('answering.html',title='Answer')


def handRealtime():
   return Response(hand_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

def handRealtime2():
    return Response(hand_detection_mode_2(), mimetype='multipart/x-mixed-replace; boundary=frame')


def quizMenu():
    return render_template('quizmenu.html',title='Quiz Menu')

def createQuizQuestion():
    return render_template('createQuestion.html',title='Create Quiz Question')


def questionSummary():
    return render_template('questionSummary.html',title='Question Summary')


def reportSummary():
    return render_template('reportSummary.html',title='Report Summary')