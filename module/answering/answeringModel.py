
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.questions.questionsClass import Question


def answering():
    #ans=fingerCount.sendConfirmedOption
    quizroom_id=session['quizroom_id']
    stores=[]
    stores=Question.display_all_question(quizroom_id)
    print("stores",stores)
    return render_template('answering.html',title='Answer')


#def myFinalAnswer(answer):

    #print(answer)
