from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ggininder5487@127.0.0.1:3306/nkust_club"

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    std_id = db.Column(db.String(12), unique = True, nullable = False, primary_key=True)
    department = db.Column(db.String(7), unique = False, nullable = False)
    name = db.Column(db.String(10), unique = True, nullable = False)

    indentitys = db.relationship('Indentity', backref = 'student')
    

class Club(db.Model):
    __tablename__ = 'club'
    club_id = db.Column(db.String(12), unique = True, nullable = False, primary_key=True)
    name = db.Column(db.String(10), unique = True, nullable = False)
    indentity = db.relationship('Indentity', backref = 'club')

class Indentity(db.Model):
    __tablename__ = 'indentity'
    pid = db.Column(db.Integer, primary_key = True)
    std_id = db.Column(db.String(12), db.ForeignKey('student.std_id'))
    club_id = db.Column(db.String(12), db.ForeignKey('club.club_id'))
    job = db.Column(db.Integer, nullable = False)

