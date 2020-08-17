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
    

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code , 200)
        

if __name__ == "__main__":
    unittest.main()