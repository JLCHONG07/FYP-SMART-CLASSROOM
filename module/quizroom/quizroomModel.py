
from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
import uuid
from module.quizroom.quizroomClass import Quizroom

def quizrooms():  
    email=session['email']
    if Quizroom.quizroom_exists(email):   
        create_quizroom=Quizroom.display_all_quizrooms(email)
        quizroom=create_quizroom['quizrooms']
        print(quizroom)

        return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=quizroom)  
    
    else:
        return render_template('quizRoom.html',title='Smart Quiz',create_quizroom=[])

def create_quizroom():


    subject="subject"
    #_id = 123456789
    total_progress=20
    assigned_to="Group 5"
    quiz_code="123456"
    belongs_to=session["email"]
    #print(_id)
    #classroom=[]
    #classroom=Classroom(_id=_id,subject=subject,total_progress=total_progress,assigned_to=assigned_to,class_code=class_code,belongs_to=belongs_to)
    Quizroom.create_new_quizroom(subject,total_progress,assigned_to,quiz_code,belongs_to,_id=None)
    return redirect(url_for('smartQuiz'))



    
   