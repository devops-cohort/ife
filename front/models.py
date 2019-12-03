from front import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.user_name
        ])

class Character(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     character_name = db.Column(db.String(200), nullable=False)
     level = db.Column(db.Integer, nullable=False, default='1')
     race = db.Column(db.String(20), nullable=False)
     character_class = db.Column(db.String(30), nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     def __repr__(self):
         return ''.join([
             'Name: ', self.character_name, '\r\n',
             'lvl: ', int(self.level), '\r\n',
             'Race: ', self.race, '\r\n',
             'Class: ', self.character_class

        ])

class Campaign(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     camp_name = db.Column(db.String(500), nullable=False)
     start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     end_date = db.Column(db.DateTime, nullable=False, default='TBD')
     status = db.Column(db.String(20), nullable=False)
     character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

     def __repr__(self):
         return ''.join([
             'Campaign: ', self.camp_name, '\r\n',
             'Start Date: ', self.start_date, '\r\n',
             'Finish Date: ', self.end_date, '\r\n',
             'Status: ', self.status
        ])
