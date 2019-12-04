from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from front.models import User


class RegistrationForm(FlaskForm):


    user_name = StringField('User Name',
            validators=[
                DataRequired(),
                Length(min=2, max=30)
            ]
    )
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )
    password = PasswordField('Password',
            validators=[
                DataRequired()
            ]
        )

    confirm_password = PasswordField('Confirm Password',
            validators=[
                DataRequired(),
                EqualTo('password')
            ]
        )


    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()


        if user:
            raise ValidationError('Email is already in use!')

    
class LoginForm(FlaskForm):
    user_name = StringField('User Name',
            validators=[
                DataRequired(),
                
            ]
        )
    password = PasswordField('Password',
            validators=[
                DataRequired()
            ]
        )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

