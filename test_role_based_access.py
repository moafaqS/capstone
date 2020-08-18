import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import patch
from functools import wraps
from app import create_app
from models import setup_db,  Movie, Actor

casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3YzY3M2VkYzEwMDNkNjUwMDY2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzAyMTIsImV4cCI6MTU5NzgxNjYxMCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.dgbD_StKSbU3GsL9qHSkkrk1kkUo6R27k3jKiBAnfiyMJOtYx-n9Ebp_4_WpHug6s8_xGs7eR-09ttA_MJT07_p7L0O-sM2WX0GuefC8KDQAVu2LpcKIjDmFc5Sphkt-AdxoWWXcdq0fbTT4AEgnk-wkvW1CZu3lNCyKVmkC7YeG9s6R8MGPZwAtCfscd2_fJ2p3_zQeMs59-I8AicDgdfwtTgIKEp7219Mw6XeeoPq1r_0qPPCgqLccwCT5sNRmBIskBLEmvXShzQf8H0xYfXvWTE2DLRKz5RM5CnwDcettzQuk4osHzOz3_lpAN2pK7_p8l-EAWY3sDDf0R-zZHw'


casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3Zjc2YWE4MDUwMDM3Njg4Mjk3IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzA0ODIsImV4cCI6MTU5NzgxNjg4MCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.TR4tNqHjjD1RbNbgE3TRMmoeMrTsLc11S1t2Zinh--g41ycS2qw8lITaOW6gmwCw4hP4lUTY_3u3H8p9-K21yEQBIivXrmxc9R6wuJMh1CsBmps2f18FpIrEtUQmjbNJGfCenFghVBGXikiUUnBgvn-ybXDnWMVFJ1AiRaYd5ioj5RJtZXtPfn1lVDrP0Rl20zLcf8DuVM1nHjLsoK0GY8q6DQBxRRE-74mC6bth8XlO8QUqIo9AYLSJxr6IMSM3uBiXPF9aNzHtbz8sp4asR_5kHEHJUm2Lw4PhfvZLQ7FwkC0e0c-Zz44NZT8cLOYwAToWkgV2Gn1dL4JsTJReWA'


executive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M4MTA3M2VkYzEwMDNkNjUwMDk2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzAzNTAsImV4cCI6MTU5NzgxNjc0OCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6bW92aWVzIl19.nKw1E35jUZNWDKvrJuWlwM0JqEE7kj_ubmPfT--fRrZgs5mIhMz0gVlT1JgP8KmZXf-1uUDxhy1WHo8Lv9fjEOgO9zOK_zMcP1OJsdVjaD-YM5obLjdQQVrDo4hAVk6hw_7KVXITXQqatnrrqPcCYI6isazbaKV3lU76hlQagm1KK5xK4VrvIm9DsSuS9Iq6UeblPA0hX2-DmJxwhAMUyNRvx1XLZ5R93PlO4bVja6TGgRmuuGIEcwSrHidXCLFKLpbNj7dsZPr6zZ4B1BHhnvr3-1Q2yEZPhaYk506z4_AXlzmz00eW22ePOO3W5J_IS1Xp2kTZhZhbjK1_mkVqYg'



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

    

    

   
    def test_Casting_Assistant_pass(self):
        res = self.client().get('/movies' , headers={
                                    "Authorization": "Bearer {}".format(
                                        casting_assistant)
                                })
        self.assertEqual(res.status_code, 200)

    def test_Casting_Assistant_fail(self):
        res = self.client().delete('/movies/delete/1' , headers={
                                    "Authorization": "Bearer {}".format(
                                        casting_assistant)
                                })
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Permission not found.')

    
    def test_executive_producer_pass(self):
        movie = {
            'title': 'the matrix',
            'releaseDate' : '2019',
        }
        res = self.client().post('/movies' ,json=movie ,headers={
                                    "Authorization": "Bearer {}".format(
                                        executive_producer)
                                })
        self.assertEqual(res.status_code, 200)

    def test_executive_producer_fail(self):
        actor = {}
        res = self.client().post('/actors' ,json=actor ,headers={
                                    "Authorization": "Bearer {}".format(
                                        executive_producer)
                                })
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Permission not found.')


    def test_casting_director_pass(self):
        actor = {
            'name': 'moafaq',
            'age' : '25',
            'Gender' : 'male'
        }
        res = self.client().post('/actors' ,json=actor ,headers={
                                    "Authorization": "Bearer {}".format(
                                        casting_director)
                                })
       
        self.assertEqual(res.status_code, 200)



    def test_casting_director_fail(self):
        movie = {
            'title': 'the matrix',
            'releaseDate' : '2019',
        }
        res = self.client().post('/movies' ,json=movie ,headers={
                                    "Authorization": "Bearer {}".format(
                                        casting_director)
                                })
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Permission not found.')



        





if __name__ == "__main__":
    unittest.main()