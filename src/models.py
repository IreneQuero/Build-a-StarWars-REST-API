from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
           
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))

    def __repr__(self):
        return '<People %r>' % self.name

    
    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "population": self.population,
            "climate": self.climate,
        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey('user.email'))
    people = db.Column(db.Integer, db.ForeignKey('people.id'))
    user_fav = db.relationship('User')
    favorite_people = db.relationship('People')  

    def __repr__(self):
        return '<Favorite %r>' % self.id

    
    def serialize(self):
        return {
            "user": self.user_fav,
            "people": self.people,
            "is_active": self.is_active
        }
