
from flask import Flask,render_template,Response,request,redirect,url_for,flash
import flask
from flask.globals import session
import uuid
from module.answering.answeringClass import Answer
from module.quizroom.quizroomClass import Quizroom
from module.account.accountClass import User



def reportSummary():
      return render_template('reportSummary.html',title='Report Summary')