
from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
import uuid
from module.quizroom.quizroomClass import Quizroom

def quizrooms(editCreated):  
    email=session['email']
    if Quizroom.quizroom_exists(email):   
        create_quizroom=Quizroom.display_all_quizrooms(email)
        #print(create_quizroom)
        #quizroom=create_quizroom['quizrooms']
        #print(quizroom)
        if request.method=="POST":
            if request.form.get('submit')=='Go':
                _id=request.form.get("quiz-room-id")
                print(_id)
                
                return render_template('quizmenu.html',title='Quiz Menu')
            elif request.form.get('submit')=='Edit':
                name=request.form.get("quiz-room-name")
                print(name)
                editCreated=False
                return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=create_quizroom,editTrue=editCreated)


        return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=create_quizroom,editTrue=editCreated)  
    else:
         return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=[],editTrue=editCreated)  

    

def create_quizroom():


    subject="subject(1)"
    _id = uuid.uuid4().hex
    total_progress=0
    total_student=0
    assigned_to="Edit to select group to assign"
    quiz_code=None
    belongs_to=session["email"]
    #print(_id)
    quizrooms=[
        subject,
        total_progress,
        assigned_to,
        quiz_code,
        total_student,
        _id]
    #classroom=Classroom(_id=_id,subject=subject,total_progress=total_progress,assigned_to=assigned_to,class_code=class_code,belongs_to=belongs_to)
    Quizroom.create_new_quizroom(belongs_to,quizrooms,_id=None)
    return redirect(url_for('smartQuiz'))


     





    
   