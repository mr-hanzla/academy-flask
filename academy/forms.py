from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, AnyOf, ValidationError
from academy.models import User

USER_TYPE_CHOICES = [
    ('ADM', 'Admin'),
    ('TCH', 'Teacher'),
    ('STU', 'Student'),
    ('MGM', 'Management'),
]

class RegisterUserForm(FlaskForm):
    def validate_username(self, form_username):
        user = User.query.filter_by(username=form_username.data).first()
        if user:
            raise ValidationError(f'Username [{form_username.data}] already exists. Try a different username')
    
    def validate_email(self, form_email):
        user = User.query.filter_by(email=form_email.data).first()
        if user:
            raise ValidationError(f'User with email:[{form_email.data}] alread present. Try a different email address.')

    username = StringField(label='User Name', validators=[Length(min=4, max=20), DataRequired()])
    email = EmailField(label='Email Address', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=6)])
    password2 = PasswordField(label='Conirm Password', validators=[EqualTo('password1')])
    user_type = SelectField(label='User Type', choices=USER_TYPE_CHOICES, validators=[DataRequired(), AnyOf([i for i, j in USER_TYPE_CHOICES])])
    submit = SubmitField(label='Register User')

class LoginUserForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

