from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, AnyOf

USER_TYPE_CHOICES = [
    ('ADM', 'Admin'),
    ('TCH', 'Teacher'),
    ('STU', 'Student'),
    ('MGM', 'Management'),
]

class RegisterUserForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=4, max=20), DataRequired()])
    email = EmailField(label='Email Address', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=6)])
    password2 = PasswordField(label='Conirm Password', validators=[EqualTo('password1')])
    user_type = SelectField(label='User Type', choices=USER_TYPE_CHOICES, validators=[DataRequired(), AnyOf(['admin', 'teacher', 'student', 'tadmin', 'sadmin', 'madmin'])])
    submit = SubmitField(label='Register User')

class LoginUserForm(FlaskForm):
    username = StringField(label='User Name')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Sign in')

