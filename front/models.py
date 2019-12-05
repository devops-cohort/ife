from front import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    charas = db.relationship('Chara', backref='creator', lazy=True)
    camps = db.relationship('Campaign', backref='master', lazy=True)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.user_name
        ])

class Chara(db.Model):
     Charaid = db.Column(db.Integer, primary_key=True, autoincrement=True)
     character_name = db.Column(db.String(200), nullable=False)
     level = db.Column(db.Integer, nullable=False, default='1')
     race = db.Column(db.String(20), nullable=False)
     character_class = db.Column(db.String(30), nullable=False)
     dm = db.Column(db.String(30), db.ForeignKey('user.user_name'), nullable=False)
    


     def __repr__(self):
         return ''.join([
             'Name: ', self.character_name, '\r\n',
             'lvl: ', int(self.level), '\r\n',
             'Race: ', self.race, '\r\n',
             'Class: ', self.character_class

        ])

class Campaign(db.Model):
     Campid = db.Column(db.Integer, primary_key=True, autoincrement=True)
     camp_name = db.Column(db.String(500), nullable=False)
     start_date = db.Column(db.String(10), nullable=False)
     end_date = db.Column(db.String(10), nullable=False)
     status = db.Column(db.String(20), nullable=False)
     dm = db.Column(db.String(30), db.ForeignKey('user.id'), nullable=False)
     group = db.relationship('Campaign', secondary=group, backref= 'member', lazy=True)

    

     def __repr__(self):
         return ''.join([
             'Campaign: ', self.camp_name, '\r\n',
             'Start Date: ', self.start_date, '\r\n',
             'Finish Date: ', self.end_date, '\r\n',
             'Status: ', self.status, '\r\n',
             'Dungeon Master: ', self.dm
        ])

group = db.Table('group', db.Model.metadata,
        db.Column('Campid', db.Integer, db.ForeignKey('campaign.Campid')),
        db.Column('Charaid', db.Integer, db.ForeignKey('chara.Charaid'))
