from flask import render_template


def instruction():
    return render_template('instructionAnswering.html',title='Instruction')

