import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

#database_name = "Capstone"
#database_path = "postgres://{}/{}".format('localhost:5432', database_name)

ENV = 'dev'

if ENV == 'dev':
    database_name = "Capstone"
    database_path = "postgres://{}/{}".format('localhost:5432',database_name)
else:
    database_name = "Capstone"
    database_path = os.environ['DATABASE_URL']
    conn = psycopg2.connect(database_path, sslmode='require')


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''   
def setup_app():
  # create and configure the app
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

  CORS(app)
  return app
'''

class Movie(db.Model):
  __tablename__ = 'Movie'
  id =  db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  releaseDate = db.Column(db.String)

  def __init__(self, title, releaseDate):
    self.title = title
    self.releaseDate = releaseDate

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'releaseDate': self.releaseDate}

  def insert(self):
    db.session.add(self)
    db.session.commit() 

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit() 

class Actor(db.Model):
  __tablename__ = 'Actor'
  id =  db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  age = db.Column(db.Integer)
  gender = db.Column(db.String)

  def __init__(self, name, age , gender):
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender}

  def insert(self):
    db.session.add(self)
    db.session.commit() 

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit() 





