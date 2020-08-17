import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

        def test_get_movies(self):
            res = self.client().get('/Movies')
            data = json.loads(res.data)

            self.assertEqual(res.status_code , 200)
            self.assertEqual(data['success'],True)
            self.assertTrue(len(data['Movies']))