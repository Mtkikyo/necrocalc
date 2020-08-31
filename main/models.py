from main import db
from flask_sqlalchemy import SQLAlchemy

class Maneuver(db.Model):
    name = db.Column(db.Text)
    category = db.Column(db.Text)
    damage = db.Column(db.Integer)
    dicead = db.Column(db.Integer)
    twice = db.Column(db.Text)
    multi = db.column(db.Text)
    cost = db.column(db.Integer)

    def __repr__(self):
        return self.name

class Skill(db.Model):
    name = db.Column(db.Text)
    category1 = db.Column(db.Text)
    category2 = db.Column(db.Text)
    damage = db.Column(db.Integer)
    dicead = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    
    def __repr__(self):
        return self.name

def init():
    db.create_all()