from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session

def instruction():
    return render_template('instructionAnswering.html',title='Instruction')

