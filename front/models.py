from application import db

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
     level = db.Column(db.Integer(2), nullable=False, default='1')
     race = db.Column(db.String(20), nullable=False)
     character_class = (db.String(30), nullable=False)

     def __repr__(self):
         return ''.join([
             'Name: ', self.character_name, '\r\n',
             'lvl: ', int(self.level), '\r\n',
             'Race: ', self.race, '\r\n',
             'Class: ', self.character_class

        ])


