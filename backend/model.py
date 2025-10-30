from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class pizza(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    toppings = db.Column(db.String(100), nullable = False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(100), nullable = False, default ='User')
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
