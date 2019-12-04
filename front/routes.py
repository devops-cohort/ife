from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from front import app, db, bcrypt
from front.models import User, Chara, Campaign
from front.forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara')
@login_required
def character():
    characterData= Chara.query.all()
    return render_template('character.html', title='Character', characters=characterData)

@app.route('/camp')
@login_required
def campaign():
    campaignData= Campaign.query.all()
    return render_template('campaign.html', title='Campaign', campaigns=campaignData)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chara'))

    form = LoginForm()
    if form.validate_on_submit():
        user =User.query.filter_by(user_name=form.user_name.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(
                user_name = form.user_name.data,
                email = form.email.data,
                password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


