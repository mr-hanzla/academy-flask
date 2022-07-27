from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField

class RegisterUserForm(FlaskForm):
    username = StringField(label='User Name')
    email = EmailField(label='Email Address')
    password1 = PasswordField(label='Password')
    password2 = PasswordField(label='Conirm Password')
    user_type = StringField(label='User Type')
    submit = SubmitField(label='Register User')


