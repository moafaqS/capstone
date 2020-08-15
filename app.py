import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import create_app, Movie, Acors

APP = create_app()



'''
Movies End points
'''
@APP.route('/movies' , methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify({
        'success': True,
        'Movies': [movie.format() for movie in movies]
    }), 200

@APP.route('/movies/<int:id>')
def get_movie(id):
  
  try:
    movie = Movie.query.filter(Movie.id == id).one_or_none()

    return  jsonify({
      'success' : True , 
      'Movies' : movie.format()
    })
  except:
    abort(404)

@APP.route('/movies' , methods=['POST'])
def post_movie():
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

@APP.route('/movies/<int:id>' , methods=['DELETE'])
def delete(id):

  try:
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    movie.delete()
    return jsonify({"success": True, "delete": id})
  except:
    abort(422)


@APP.route('/movies/<int:id>' , methods=['PATCH'])
def update(id):
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



'''
Error Handler
'''
@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@APP.errorhandler(404)
def resourceNotFound(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404




if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)