
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.quizroom.quizroomClass import Quizroom


##things to do:
    #add delete feature
    #hide important field eg _id
    #remove uncessary background color
    ###optional: make edit feild to look better

def quizrooms():  
    email=session['email']
    if Quizroom.quizroom_exists(email):   
        create_quizroom=Quizroom.display_all_quizrooms(email)
        #print(create_quizroom)
        #quizroom=create_quizroom['quizrooms']
        #print(quizroom)
        if request.method=="POST":
            session.pop("_flashes",None)
            if request.form.get('submit')=='Go':
                _id=request.form.get("quiz-room-id")
                
                print(_id)
                if Quizroom.get_a_quizroom(_id,email):
                  
                    print("Quizroom exists")
                    return render_template('quizmenu.html',title='Quiz Menu')
                else:
                    invalid="Please Select a Quizroom Below"
                    flash(invalid,'quizroom_invalid_error')
                    print("No select Quizroom")
                    return redirect(url_for('smartQuiz'))
                
            elif request.form.get('submit')=='Edit':
                session.pop("_flashes",None)
                _id=request.form.get("edit-quiz-room-id")
                subject_name=request.form.get("quiz-room-name")
                assign_to_group=request.form.get("edit-group-assigned")
                #print(_id)
                #print(subject_name)
                #print(assign_to_group)
                if Quizroom.edit_quiz_room(_id,email,subject_name,assign_to_group):
                    #print("Successful updated")
                    return redirect(url_for('smartQuiz'))
            elif request.form.get('submit')=="Delete":
                _id=request.form.get("edit-quiz-room-id")
                confirm_message=request.form.get("delete-confirmation")
                #print(_id)
                #print(confirm_message)
                if confirm_message == "Confirm":
                    #print(confirm_message)
                    if Quizroom.delete_quiz_room(_id,email):
                        print("Successful delete")
                        return redirect(url_for('smartQuiz'))
                else:
                   # invalid_confirm="Confirm"
                    #invalid="Invalid Input Please Enter "+invalid_confirm+" Again"
                   # flash(invalid,'quizroom_edit_invalid_error')
                    return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=create_quizroom) 


        return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=create_quizroom)  
    else:
         return render_template('quizRoom.html',title='Smart Quiz',created_quizroom=[])  

    

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


     





    
   