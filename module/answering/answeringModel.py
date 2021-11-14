
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.questions.questionsClass import Question
import pyautogui

def answering():
    #ans=fingerCount.sendConfirmedOption
    quizroom_id=session['quizroom_id']
    #print("quizroom_id",quizroom_id[0])

    question_number=session['Question_No']
    print(question_number)
    stores=[]
    questions=Question.display_all_question(quizroom_id)
    #print("stores",questions)
    all_ans=[]
    all_questions=[]
    all_answer1=[]
    all_answer2=[]
    all_answer3=[]
    all_answer4=[]
 

    for answer in questions['question_set']:
            all_questions.append(answer['question'])
            all_answer1.append(answer['answer1'])
            all_answer2.append(answer['answer2'])
            all_answer3.append(answer['answer3'])
            all_answer4.append(answer['answer4'])
    #print(all_answer1[question_number-1])
    
    if request.method=="POST":
        if request.form.get('submit')=="Next":
            total_questions=len(all_questions)
            print("total questions:",total_questions)
            question_number+=1
            if question_number <= total_questions:
                session['Question_No']=question_number
            else:
                session['Question_No']=1

        return redirect(url_for('answering'))
    
    for a in questions['question_set']:
        all_ans.append(a['correct_answer'])
    ##print(all_ans)
    #print(all_ans[0])
    return render_template('answering.html',title='Answer',
    questions=all_questions[question_number-1],
    question_no=question_number,
    answer1=all_answer1[question_number-1],
    answer2=all_answer2[question_number-1],
    answer3=all_answer3[question_number-1],
    answer4=all_answer4[question_number-1],)


#def myFinalAnswer(answer):

    #print(answer)
