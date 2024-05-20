from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance without binding it to the app yet
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)

class Request(db.Model):
    email = db.Column(db.String(200), primary_key=True)
    shift = db.Column(db.String(200), nullable=False)
    reason = db.Column(db.String(1000), nullable=False)
    role = db.Column(db.String(1000), nullable=False)

class Needs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    needs = db.Column(db.String(500), nullable=False)

class Schedule(db.Model):
    email = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(1000), nullable=False)
    shift = db.Column(db.String(1000), nullable=False)
    time = db.Column(db.String(1000), nullable=False)
    role = db.Column(db.String(120), nullable=False)

class Prisoner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)
    birth = db.Column(db.String(120), nullable=False)
    record = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(120), nullable=False)
    cell = db.Column(db.String(120), nullable=False)