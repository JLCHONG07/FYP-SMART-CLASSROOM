import uuid
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
from module.questions.questionsClass import Question
from module.quizroom.quizroomClass import Quizroom
from appForm import questionForm

def questionSummary():
    quizroom_id=session['quizroom_id']
    questions=Question.display_all_question(quizroom_id)
    #print(questions)
    #for x in questions:
        #print(x)
    if request.method=="POST":
        if request.form.get("submit")=="Edit":
            question_id=request.form.get("question-list-id")
            print(question_id)
            session['question_id']=question_id
            return redirect(url_for('createQuizQuestion'))

        else:
            #session.pop('question_id',None)
            session['question_id']=None
            return redirect(url_for('createQuizQuestion'))

    return render_template('questionSummary.html',title='Question Summary',questions=questions)

def createQuestion():
    question_id=session['question_id']
    form=questionForm()
    form2=questionForm()
    #check is that the question is click from questionSummary
    #if yes then retrieve the data based on the question_id
    
    question_id=Question.search_question_id(question_id)
    edit_id=None
        #print(question_id)
    if question_id is not None:
        for question in question_id:
                #after retreived the data assign back to form input
                #hence the form input has the value
            edit_id=question.get('question_set')[0].get('_id')
            form2.question.data=question.get('question_set')[0].get('question')
            form2.answer1.data=question.get('question_set')[0].get('answer1')
            form2.answer2.data=question.get('question_set')[0].get('answer2')
            form2.answer3.data=question.get('question_set')[0].get('answer3')
            form2.answer4.data=question.get('question_set')[0].get('answer4')
            form2.correct_answer.data=question.get('question_set')[0].get('correct_answer')
        if request.method=="POST":
            quizroom_id=session['quizroom_id']
            #print(quizroom_id)
            question=form.question.data
            answer1=form.answer1.data
            answer2=form.answer2.data
            answer3=form.answer3.data
            answer4=form.answer4.data
            correct_ans=form.correct_answer.data
            if form.submit.data:
                if edit_id is None:
                    question_id=uuid.uuid1().hex
                    #print(question,answer1,answer2,answer3,answer4,correct_ans)
                    question_set=[question_id,question,answer1,answer2,answer3,answer4,correct_ans]
                    Question.get_created_question(quizroom_id,question_set,_id=None)
                    Quizroom.update_total_quizroom_score(quizroom_id,total_update_scores=10)
                    return redirect(url_for("questionSummary"))
                else:
                    question_id=edit_id
                    #question_set=[question_id,question,answer1,answer2,answer3,answer4,correct_ans]
                    Question.edit_question(question_id,question,answer1,answer2,answer3,answer4,correct_ans)
                    session['question_id']=None
                    return redirect(url_for("questionSummary"))
            elif form.delete.data:
                    session['question_id']=None
                    Question.delete_question(edit_id)
                    Quizroom.update_total_quizroom_score(quizroom_id,total_update_scores=-10)
                    return redirect(url_for("questionSummary"))
            else:
                    session['question_id']=None
                    return redirect(url_for("questionSummary"))
        return render_template('createQuestion.html',title='Create Quiz Question',form=form2)
    return render_template('createQuestion.html',title='Create Quiz Question',form=form)

