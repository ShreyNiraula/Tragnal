from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from tragnal2.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    age = IntegerField('Age', validators=[DataRequired()])

    submit = SubmitField('Register')

    # these two function are used in checking if the same
    # named user exist when registering
    # def validate_field(self, field): is default format
    # replace field with any field actually in models
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username used, choose another username')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email exists for other user, choose another email')

class LoginForm(FlaskForm):
    #login by email
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_Me')
    submit = SubmitField('Login ')