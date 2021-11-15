
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.answering.answeringClass import Answer
from module.questions.questionsClass import Question
import pyautogui



def answering():
    #ans=fingerCount.sendConfirmedOption
    quizroom_id=session['quizroom_id']
    #print("quizroom_id",quizroom_id[0])
    #session['answered']=0
    question_number=session['Question_No']
    email=session['email']
    points=0
    remarks=None
    submitOrNext="Next"

    #print(question_number)
    
    questions=Question.display_all_question(quizroom_id)
    answered_details=Answer.get_answered_details(quizroom_id,email)
    print("answered_details",answered_details)
    questions_array=question_number-1
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

 

    for answer in questions['question_set']:
            all_questions.append(answer['question'])
            all_answer1.append(answer['answer1'])
            all_answer2.append(answer['answer2'])
            all_answer3.append(answer['answer3'])
            all_answer4.append(answer['answer4'])
            all_ans.append(answer['correct_answer'])
            all_questions_id.append(answer['_id'])
    #print(all_answer1[question_number-1])
    for answered_details in answered_details:
        for answered_set in answered_details['answered_set']:
                print(answered_set['selected_answer'])
    
    if request.method=="POST":
        if request.form.get('submit')=="Next":
            total_questions=len(all_questions)
            print("total questions:",total_questions)
            question_number+=1
            if question_number <= total_questions:
                session['Question_No']=question_number
                submitOrNext="Next"
            else:
                #ending
                session['Question_No']=1
            return redirect(url_for('answering'))
        elif request.form.get('submit')=="CheckAnswer":
                question_id=all_questions_id[questions_array]
                selected_answered=Answer._answered
                correct_answer=all_ans[questions_array]
                remark=None
                answered_set=[question_id,selected_answered,correct_answer,remark]
                Answer.save_with_check(quizroom_id,email,points,answered_set)
                submitOrNext="Submit"
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
    submitOrNext=submitOrNext)


