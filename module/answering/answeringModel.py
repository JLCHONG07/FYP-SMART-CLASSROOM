
from flask import render_template,request,redirect,url_for,flash
from flask.globals import session
from module.answering.answeringClass import Answer
from module.questions.questionsClass import Question
from module.quizroom.quizroomClass import Quizroom
from module.ranking_report.reportClass import Report



def answering():
   
    quizroom_id=session['quizroom_id']
    #print("quizroom_id",quizroom_id[0])
    question_number=session['Question_No']
    email=session['email']
    current_points=session['points']
    submitOrNext="Next"
    ending=session['ending']
    #print(question_number)
    total_questions=0
    questions=Question.display_all_question(quizroom_id)
    #print(questions)
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
    all_points=[]

    #Add the question, answer1, answer2, answer3, answer4, correct answer and question id to array
    #This is use for displsying the question and answers depend on the question no
    if questions is not None:
        for answer in questions['question_set']:
                all_questions.append(answer['question'])
                all_answer1.append(answer['answer1'])
                all_answer2.append(answer['answer2'])
                all_answer3.append(answer['answer3'])
                all_answer4.append(answer['answer4'])
                all_ans.append(answer['correct_answer'])
                all_questions_id.append(answer['_id'])

    else:
        #When click on the start now, if the question_set is empty it will return the message "Questions is not ready yet"
        #Which mean the admin havent add the question for this quizroom
        invalid_questions="Questions is not ready yet"
        flash(invalid_questions,"invalid_questions")
        return redirect(url_for("instruction"))
    #print(all_answer1[question_number-1])
    
    if request.method=="POST":

        if request.form.get('submit')=="Next":
            total_questions=len(all_questions)
            #print("total questions:",total_questions)
            submitOrNext="Next"
            question_number+=1

            if question_number <= total_questions:
                session['Question_No']=question_number
                #Reset the selected answer to default to avoid it get the previous selected answer
                Answer._answered="0"

            else:
                #print("ending")
                session['ending']=True
                save_email=email
                save_points=current_points
                progress="complete"
                user_answered_details=[save_email,save_points]
                check_new_user_answer=Answer.new_answer_user(email,quizroom_id,progress)
                #print("check_new_user_answer",check_new_user_answer)
                if check_new_user_answer:
                    Quizroom.update_student_progress(quizroom_id)
                    Report.save_report(quizroom_id,user_answered_details,_id=None)

            return redirect(url_for('answering'))

        elif request.form.get('submit')=="CheckAnswer":
                submitOrNext="Submit"
                #ending=session['ending']
                question_id=all_questions_id[questions_array]
                selected_answered=Answer._answered
                print("selected_answered",selected_answered)
                correct_answer=all_ans[questions_array]
                remark=None
                _id=None
                progress="pending"
                answered_set=[question_id,selected_answered,correct_answer,remark]
                Answer.save_with_check(quizroom_id,email,current_points,progress,answered_set,_id)
                answered_details=Answer.get_answered_details(quizroom_id,email)
                #print("answered_details",answered_details)
                #This is use for retrieve the stored data in answer database 
                #Use for display the result after submit
                #It will display the answer depend on question no
                for answered_details in answered_details:
                    for answered_set in answered_details['answered_set']:
                        all_selected_answer.append(answered_set['selected_answer'])
                        all_correct_answer.append(answered_set['correct_answer'])
                        all_remarks.append(answered_set['remark'])

                        all_points.append(answered_details['points'])
                answered_array=0
                total_answered=len(all_selected_answer)
         
                #print(total_answered)
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
                
        elif request.form.get('submit')=="BackMenu":
                #print("Back to Menu")
                session['ending']=False
                session['Question_No']=1
                session['points']=0
                return redirect(url_for('quizMenu'))
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


