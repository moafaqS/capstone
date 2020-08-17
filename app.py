import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth 



def create_app():
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)
  cors = CORS(app, resources={r"/": {"origins": "*"}})



  '''
  Movies End points
  '''
  @app.route('/movies' , methods=['GET'])
  def get_movies():
      movies = Movie.query.all()
      return jsonify({
          'success': True,
          'Movies': [movie.format() for movie in movies]
      }), 200

  @app.route('/movies/<int:id>')
  @requires_auth('get:movies')
  def get_movie(jwt,id):
    
    try:
      movie = Movie.query.filter(Movie.id == id).one_or_none()

      return  jsonify({
        'success' : True , 
        'Movies' : movie.format()
      })
    except:
      abort(404)


  @app.route('/movies' , methods=['POST'])
  @requires_auth('post:movies')
  def post_movie(jwt):
    body = request.get_json()
    title = body.get('title')
    releaseDate = body.get('releaseDate')

    try:
      movie = Movie(title=title,releaseDate=releaseDate)
      Movie.insert(movie)

      return jsonify({
        'success': True,
        'Movies': [movie.format()]
      }), 200

    except:
      abort(422)

  @app.route('/movies/<int:id>' , methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(jwt,id):

    try:
      movie = Movie.query.filter(Movie.id == id).one_or_none()
      movie.delete()
      return jsonify({"success": True, "delete": id})
    except:
      abort(422)


  @app.route('/movies/<int:id>' , methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(jwt,id):
    if id is None:
      abort(404)

    try:
      body = request.get_json()
      title = body.get('title')
      releaseDate = body.get('releaseDate')

      movie = Movie.query.filter(Movie.id == id).one_or_none()
      movie.title = title
      movie.releaseDate = releaseDate
      movie.update()

      return jsonify({
        'success': True,
        'Movies': [movie.format()]
      }), 200

    except:
      abort(422)

    
    '''
  Actor End points
  '''

  @app.route('/actors' , methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(jwt):
      actors = Actor.query.all()
      return jsonify({
          'success': True,
          'actors': [actor.format() for actor in actors]
      }), 200

  @app.route('/actors/<int:id>')
  @requires_auth('get:actors')
  def get_actor(jwt,id):
    
    try:
      actor = Actor.query.filter(Actor.id == id).one_or_none()

      return  jsonify({
        'success' : True , 
        'actor' : actor.format()
      })
    except:
      abort(404)

  @app.route('/actors' , methods=['POST'])
  @requires_auth('post:actors')
  def post_actor(jwt):
    body = request.get_json()
    
    name = body.get('name')
    age = body.get('age')
    gender = body.get('Gender')
    

    try:
      actor = Actor(name=name,age=age,gender=gender)
      Actor.insert(actor)

      return jsonify({
        'success': True,
        'Movies': actor.format()
      }), 200

    except:
      abort(422)

  @app.route('/actors/<int:id>' , methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(jwt,id):

    try:
      actor = Actor.query.filter(Actor.id == id).one_or_none()
      actor.delete()
      return jsonify({"success": True, "delete": id})
    except:
      abort(422)


  @app.route('/actors/<int:id>' , methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(jwt,id):
    if id is None:
      abort(404)

    try:
      body = request.get_json()
      name = body.get('name')
      age = body.get('age')
      gender = body.get('gender')

      actor = Actor.query.filter(Actor.id == id).one_or_none()
      actor.name = name
      actor.age = age
      actor.gender = gender

      actor.update()

      return jsonify({
        'success': True,
        'Movies': actor.format()
      }), 200

    except:
      abort(422)


  '''
  Error Handler
  '''
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  @app.errorhandler(404)
  def resourceNotFound(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
      }), error.status_code

  return app

  

