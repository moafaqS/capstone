import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

def setup_app(app, database_path=database_path):
  # create and configure the app
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  db.app = app
  db.init_app(app)
  db.create_all()
  


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





