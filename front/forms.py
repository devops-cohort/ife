from flask_wtf import FlaskForm
from flask_login import LoginManager, current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from front.models import User, Campaign, Chara, group
from front import app, db


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

    def validate_user_name(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('User name is already in use!')


    
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

class UpdateAccountForm(FlaskForm):
    user_name = StringField('User Name',
            validators=[
                DataRequired(),
                Length(min=2, max=30)

            ])
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ])
    submit = SubmitField('Update')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use - Please choose Another!')

    def validate_user_name(self, user_name):
        if user_name.data != current_user.user_name:
            user = User.query.filter_by(user_name=user_name.data).first()
            if user:
                raise ValidationError('The User name is already in use - Please choose Another!')

class CharacterForm(FlaskForm):
    character_name = StringField('Character Name',
            validators=[
                DataRequired(),
                Length(min=1, max=200)
            ]
        )

    level = IntegerField('Level',
            validators=[
                DataRequired(),
                NumberRange(min=1, max=20)
            ]
        )
    race = StringField('Race',
            validators=[
                DataRequired(),
                Length(min=1, max=20)
            ]   
        )   

    character_class = StringField('Class',
            validators=[
                DataRequired(),
                Length(min=1, max=30)
            ]   
        )  


    submit = SubmitField('Create!')
    
   # def name_query():
    #    return Campaign.query.filter_by(camp_name=Campaign.camp_name)

   # select = QuerySelectField('Add to:', query_factory=name_query, allow_blank=True) 

class CampaignForm(FlaskForm):
    camp_name = StringField('Campaign',
            validators=[
                DataRequired(),
                Length(min=1, max=500)
            ]
        )

    start_date = StringField('Start Date',
            validators=[
                DataRequired()
                
            ]
        )
    end_date = StringField('End Date',
            validators=[
                DataRequired()
            ]
        )

    status = StringField('Status',
            validators=[
                DataRequired(),
                Length(min=1, max=30)
            ]
        )
    submit = SubmitField('Create!')

class DeleteAccountForm(FlaskForm):


    submit = SubmitField('Delete')
