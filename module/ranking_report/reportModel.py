
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.answering.answeringClass import Answer
from module.quizroom.quizroomClass import Quizroom
from module.account.accountClass import User
from module.ranking_report.reportClass import Report


def reportSummary():
      quizroom_id=session['quizroom_id']
      report=Report.report_exists(quizroom_id)
      #print(report)
      return render_template('reportSummary.html',title='Report Summary',report=report)