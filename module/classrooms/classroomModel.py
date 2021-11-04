
from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
import uuid
from module.classrooms.classroomClass import Classroom

def classroom():  
    email=session['email']
    if Classroom.classroom_exists(email):   
        created_classroom=Classroom.display_all_classroom(email)
        classroom=created_classroom['classroom']
        print(classroom)

        return render_template('quizRoom.html',title='Smart Quiz',created_classroom=classroom)  
    
    else:
        return render_template('quizRoom.html',title='Smart Quiz',create_classroom=[])

def create_classroom():


    subject="subject"
    #_id = 123456789
    total_progress=20
    assigned_to="Group 5"
    class_code="123456"
    belongs_to=session["email"]
    #print(_id)
    classroom=[]
    #classroom=Classroom(_id=_id,subject=subject,total_progress=total_progress,assigned_to=assigned_to,class_code=class_code,belongs_to=belongs_to)
    Classroom.create_new_classroom(subject,total_progress,assigned_to,class_code,belongs_to,_id=None)
    return redirect(url_for('smartQuiz'))



    
   