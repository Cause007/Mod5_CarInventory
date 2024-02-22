# this file will import specific tools to make sure users are giving the right information

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    id = StringField('User ID',validators = [DataRequired()])
    first_name = StringField('First Name',validators = [DataRequired()])
    last_name = StringField('Last Name',validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password',"Passwords must match.")])
    submit_button = SubmitField()
