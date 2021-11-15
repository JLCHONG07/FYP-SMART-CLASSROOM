
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.answering.answeringClass import Answer
from module.questions.questionsClass import Question
from module.quizroom.quizroomClass import Quizroom
import pyautogui



def answering():
    #ans=fingerCount.sendConfirmedOption
    quizroom_id=session['quizroom_id']
    #print("quizroom_id",quizroom_id[0])
    #session['answered']=0
    question_number=session['Question_No']
    email=session['email']
    current_points=session['points']
    remarks=None
    submitOrNext="Next"
    ending=session['ending']
    #print(question_number)
    total_questions=0
    questions=Question.display_all_question(quizroom_id)

    questions_array=question_number-1
    #answered_array=0
    #print("stores",questions)
    all_ans=[]
    all_questions=[]
    all_answer1=[]
    all_answer2=[]
    all_answer3=[]
    all_answer4=[]
    all_questions_id=[]
    all_selected_answer=[]
    all_correct_answer=[]
    all_remarks=[]
    all_points=[]

 

    for answer in questions['question_set']:
            all_questions.append(answer['question'])
            all_answer1.append(answer['answer1'])
            all_answer2.append(answer['answer2'])
            all_answer3.append(answer['answer3'])
            all_answer4.append(answer['answer4'])
            all_ans.append(answer['correct_answer'])
            all_questions_id.append(answer['_id'])
    #print(all_answer1[question_number-1])

         
    
    if request.method=="POST":
        if request.form.get('submit')=="Next":
            total_questions=len(all_questions)
            print("total questions:",total_questions)
            submitOrNext="Next"
            question_number+=1
            if question_number <= total_questions:
                session['Question_No']=question_number
             

            else:
                #ending
                #session['Question_No']=1
                print("ending")
                session['ending']=True
                Quizroom.update_student_progress(quizroom_id)
                #submitOrNext="Ending"

            return redirect(url_for('answering'))
        elif request.form.get('submit')=="CheckAnswer":
                submitOrNext="Submit"
                #ending=session['ending']

                question_id=all_questions_id[questions_array]
                selected_answered=Answer._answered
                correct_answer=all_ans[questions_array]
                remark=None
                _id=None
                answered_set=[question_id,selected_answered,correct_answer,remark]
                Answer.save_with_check(quizroom_id,email,current_points,answered_set,_id)
                answered_details=Answer.get_answered_details(quizroom_id,email)
                print("answered_details",answered_details)
                for answered_details in answered_details:
                    for answered_set in answered_details['answered_set']:
                        all_selected_answer.append(answered_set['selected_answer'])
                        all_correct_answer.append(answered_set['correct_answer'])
                        all_remarks.append(answered_set['remark'])

                        all_points.append(answered_details['points'])
                answered_array=0
                total_answered=len(all_selected_answer)
         
                print(total_answered)
                if total_answered >=1:
                    answered_array=total_answered-1
                session['points']=all_points[answered_array]
                return render_template('answering.html',title='Answer',
                questions=all_questions[questions_array],
                question_no=question_number,
                answer1=all_answer1[questions_array],
                answer2=all_answer2[questions_array],
                answer3=all_answer3[questions_array],
                answer4=all_answer4[questions_array],
                submitOrNext=submitOrNext,
                selected_answer=all_selected_answer[answered_array],
                correct_answer=all_correct_answer[answered_array],
                remarks=all_remarks[answered_array],
                points=all_points[answered_array],
                ending=ending)
                #print('response answered',answered)
    #for a in questions['question_set']:
        #all_ans.append(a['correct_answer'])
    ##print(all_ans)
    #print(all_ans[0])
    return render_template('answering.html',title='Answer',
    questions=all_questions[questions_array],
    question_no=question_number,
    answer1=all_answer1[questions_array],
    answer2=all_answer2[questions_array],
    answer3=all_answer3[questions_array],
    answer4=all_answer4[questions_array],
    submitOrNext=submitOrNext,
    selected_answer=0,
    correct_answer=0,
    remarks=0,
    points=current_points,
    ending=ending)


