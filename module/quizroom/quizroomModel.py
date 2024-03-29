
from flask import render_template,request,redirect,url_for,flash
from flask.globals import session
import uuid
from module.answering.answeringClass import Answer
from module.quizroom.quizroomClass import Quizroom
from module.account.accountClass import User

def quizrooms():  
    email=session['email']
    if Quizroom.quizroom_exists(email):   
        create_quizroom=Quizroom.display_all_quizrooms(email)
        #print(create_quizroom)
        #for x in create_quizroom:
        #    print(x)
        #print(quizroom)
        if request.method=="POST":

            session.pop("_flashes",None)
            #subject_name=request.form.get("quiz-room-name")
            if request.form.get('submit')=='Go':

                _id=request.form.get("quiz-room-id")
                #print(_id)
                #print(subject_name)
                if Quizroom.get_a_quizroom(_id,email):

                    session['quizroom_id']=_id
                    #print("Quizroom exists")
                    return render_template('quizmenu.html',title='Quiz Menu',type=session['type'])
                else:

                    invalid="Please Select a Quizroom Below"
                    flash(invalid,'quizroom_invalid_error')
                    #print("No select Quizroom")
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
                        #print("Successful delete")
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

    subject="subject"
    _id = uuid.uuid4().hex
    total_progress=0
    total_student=0
    assigned_to="Edit to select group to assign"
    quiz_code=None
    belongs_to=session["email"]
    total_scores=0
    #print(_id)
    quizrooms=[
        subject,
        total_progress,
        assigned_to,
        quiz_code,
        total_student,
        total_scores,
        _id]
    Quizroom.create_new_quizroom(belongs_to,quizrooms,_id=None)
    return redirect(url_for('smartQuiz'))

def student_quizrooms():
    
    email=session['email']
    type=session['type']
    quizrooms_id=User.get_user_joined_room(email)
    #print(quizrooms_id)
    #results=[]
    #for quizroom_id in quizrooms_id:
    result=Quizroom.display_all_joined_quizrooms(quizrooms_id)
  
    if result is not None:
        #print(result)
        #for a in result:
           # for b in a['quizrooms']:
        if request.method=="POST":

            session.pop("_flashes",None)
            if request.form.get('submit')=="Join":

                quiz_room_code=request.form.get('join-quiz-code')
                #print(quiz_room_code)
                quizroom_id=Quizroom.valid_quiz_room_code(quiz_room_code,quizrooms_id)
                #print("quizroom_id:",quizroom_id)
                Quizroom.update_total_student(quizroom_id,total_update_student=1)

                if quizroom_id is not None:
                    #print("joined quiz room")
                    session.pop("_flashes",None)
                    User.valid_add_detail(email,type,quizroom_id)
                    return redirect(url_for('studentSmartQuiz'))
                else:

                    joined_quizroom="You have joined the quizroom or entered a invalid quizroom code!"
                    flash(joined_quizroom,"joined_quizroom_warning")
                    return redirect(url_for('studentSmartQuiz'))
                    
            elif request.form.get('submit')=='Go':

                _id=request.form.get("quiz-room-id")
                #print(_id)
                if Quizroom.joined_a_quizroom(_id,quizrooms_id):

                    print("Quizroom is joined")
                    session['quizroom_id']=_id
                    session['Question_No']=1
                    session['points']=0
                    session['ending']=False
                    return render_template('quizmenu.html',title='Quiz Menu',type=session['type'])
                else:

                    invalid="Please Select a Quizroom Below"
                    flash(invalid,'quizroom_invalid_error')
                    #print("No select Quizroom")
                    return redirect(url_for('studentSmartQuiz'))
            
            elif request.form.get('submit')=='Delete':

                _id=request.form.get("delete-quiz-room-id")
                print(_id,email)
                User.quit_quizroom(_id,email)
                Quizroom.update_total_student(_id,total_update_student=-1)
                return redirect(url_for('studentSmartQuiz'))
        
        return render_template('studentQuizRoom.html',title="Smart Quiz",joined_quizroom=result)
    else:
        
        return render_template('studentQuizRoom.html',title="Smart Quiz",joined_quizroom=[])


    #return render_template('studentQuizRoom.html',title="Smart Quiz",created_quizroom=[])


     





    
   