from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from front import app, db, bcrypt
from front.models import User, Chara, Campaign
from front.forms import RegistrationForm, LoginForm, UpdateAccountForm, CharacterForm, CampaignForm 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara', methods=['Get', 'Post'])
@login_required
def character():
    roles=Chara.query.all()

    form = CharacterForm()


    if form.validate_on_submit():

        charaData = Chara(
                character_name=form.character_name.data,
                level=form.level.data,
                race=form.race.data,
                character_class=form.character_class.data,
                creator=current_user
                )

        db.session.add(charaData)
        db.session.commit()
        return redirect(url_for('home'))

    

    else:
        print(form.errors)
    
    return render_template('character.html', title='Character', form=form, roles=roles)

@app.route('/camp', methods=['GET','POST'])
@login_required
def campaign():
    form = CampaignForm()

    if form.validate_on_submit():

        campData = Campaign(
                camp_name=form.camp_name.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                status=form.status.data,
                master=current_user
                )
        db.session.add(campData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('campaign.html', title='Campaign', form=form)

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
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


