from flask import render_template
from front import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara')
def character():
    return render_template('character.html', title='Character')

@app.route('/camp')
def campaign():
    return render_template('campaign.html', title='Campaign')

@app.route('/login')
def campaign():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')


