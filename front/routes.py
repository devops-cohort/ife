from flask import render_template
from front import app
from front.models import User, Character, Campaign

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara')
def character():
    characterData= Character.query.all()
    return render_template('character.html', title='Character', characters=characterData)

@app.route('/camp')
def campaign():
    campaignData= Campaign.query.all()
    return render_template('campaign.html', title='Campaign', campaigns=campaignData)

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')


