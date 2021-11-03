from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
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