from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session
from module.questions.questionsClass import Questions
from appForm import questionForm

def questionSummary():
    return render_template('questionSummary.html',title='Question Summary')

def createQuestion():
    form=questionForm()
    if request.method=="POST":
        question=form.question.data
        answer1=form.answer1.data
        answer2=form.answer2.data
        answer3=form.answer3.data
        answer4=form.answer4.data
        correct_ans=form.correct_answer.data

        print(question,answer1,answer2,answer3,answer4,correct_ans)
     
    return render_template('createQuestion.html',title='Create Quiz Question',form=form)

