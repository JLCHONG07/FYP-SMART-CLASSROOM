from flask import Flask,render_template,Response,request,redirect,url_for,flash
from flask.globals import session

def instruction():
    return render_template('instructionAnswering1.html',title='Instruction')


def instruction2():
    return render_template('instructionAnswering2.html',title='Instruction2')

