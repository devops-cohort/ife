from flask import render_template, redirect, url_for, request
from front import app, db, bcrypt
from front.models import User, Chara, Campaign
from front.forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara')
def character():
    characterData= Chara.query.all()
    return render_template('character.html', title='Character', characters=characterData)

@app.route('/camp')
def campaign():
    campaignData= Campaign.query.all()
    return render_template('campaign.html', title='Campaign', campaigns=campaignData)

@app.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
                user_name = form.user_name.data,
                email = form.email.data,
                password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('chara'))
    return render_template('register.html', title='Register', form=form)


