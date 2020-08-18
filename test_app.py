import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import patch
from functools import wraps
from app import create_app
from models import setup_db,  Movie, Actor



def mock_decorator(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = 'testToken'
            try:
                payload = 'testToken'
            except:
                raise AuthError({
                    'code': 'invalid',
                    'description':'invalid'
                }, 401)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator


patch('app.requires_auth', mock_decorator).start()


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app , self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables

            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    

    def test_create_movie(self):
        movie = {
            'title': 'the matrix',
            'releaseDate' : '2019',
        }
        res = self.client().post('/movies', json=movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie_fail(self):
        res = self.client().post('/movies')
        self.assertEqual(res.status_code, 400)
        

    def test_create_actor(self):
        actor = {
            'name': 'moafaq',
            'age' : '25',
            'Gender' : 'male'
        }
        res = self.client().post('/actors', json=actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor_fail(self):
        res = self.client().post('/actors')
        self.assertEqual(res.status_code, 400)

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['Movies']))

    def test_get_movies_fail(self):
        res = self.client().get('/movie')
        self.assertEqual(res.status_code, 404)
        

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))
    
    def test_get_actors_fail(self):
        res = self.client().get('/actor')
        self.assertEqual(res.status_code, 404)

    
    def test_delete_movie(self):

        res = self.client().delete('/movies/delete/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/delete/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code , 404)
        self.assertEqual(data['success'], False)
        
    
    def test_delete_actor(self):

        res = self.client().delete('/actors/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code , 422)
        self.assertEqual(data['success'], False)
    
    def test_patch_movie(self):
        movie = {
            'title': 'the matrix',
            'releaseDate' : '2019',
        }
        res = self.client().patch('/movies/18' , json=movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movie_fail(self):
        movie = {
            'title': 'the matrix',
            'releaseDate' : '2019',
        }
        res = self.client().patch('/movies/2000', json=movie)
        self.assertEqual(res.status_code, 422)


    def test_patch_actor(self):
        actor = {
            'name': 'moafaq',
            'age' : '25',
            'Gender' : 'male'
        }
        res = self.client().patch('/actors/2', json=actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_actor_fail(self):
        actor = {
            'name': 'moafaq',
            'age' : '25',
            'Gender' : 'male'
        }
        res = self.client().patch('/actors/2000', json=actor)
        self.assertEqual(res.status_code, 404)



 





if __name__ == "__main__":
    unittest.main()