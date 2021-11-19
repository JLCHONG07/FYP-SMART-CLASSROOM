from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.fields.core import SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired,Email,Length

#This section is form control which is all the input handling with validation
class loginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Length(max=50)],render_kw={"placeholder": "Please Enter Your Email"})
    psw=PasswordField('password',validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder": "Please Enter Your Password"})

class registerForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Length(max=50)],render_kw={"placeholder": "Please Enter Your Email"})
    psw=PasswordField('password',validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder": "Please Enter Your Password"})
    icno=StringField('icno',validators=[DataRequired(),Length(max=50)],render_kw={"placeholder": "Please Enter Your Ic Number"})

class quizroomForm(FlaskForm):
    subject=StringField('subject',validators=[DataRequired()],render_kw={"placeholder": "Click Any Quiz Room Below to Go"})
    assign_to=StringField('assign_to',validators=[DataRequired()])
    confirmation=StringField('confirmation',validators=[DataRequired()],render_kw={"placeholder": "Enter Confirm to Delete"})

class questionForm(FlaskForm):
    question=StringField('question',validators=[DataRequired()],render_kw={"placeholder": "Type a Question"})
    answer1=StringField('answer1',validators=[DataRequired()],render_kw={"placeholder": "Option 1"})
    answer2=StringField('answer2',validators=[DataRequired()],render_kw={"placeholder": "Option 2"})
    answer3=StringField('answer3',validators=[DataRequired()],render_kw={"placeholder": "Option 3"})
    answer4=StringField('answer4',validators=[DataRequired()],render_kw={"placeholder": "Option 4"})
    correct_answer=SelectField("correct_answer",validators=[DataRequired()],
    choices=[('a0','Correct Answer'),('a1','Option 1'),('a2','Option 2'),('a3','Option 3'),('a4','Option 4')])
    submit=SubmitField(label="Submit")
    delete=SubmitField(label="Delete")
    cancel=SubmitField(label="Cancel")