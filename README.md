# Casting Agency 
This project is the final project for the Udacity Full Stack Developer Nanodegree 

Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.


## Roles
    Casting Assistant:
        Can view actors and movies
    Casting Director:
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies
    Executive Producer:
        All permissions a Casting Director has and…
        Add or delete a movie from the database
        
# Dependencies:

For this project you need to intall Python3 (https://www.python.org/) 
Make sure to install the following packages afterward:
1.	Flask
2.	Flask-Migrate
3.	Flask-Script
4.	Flask-SQL Alchemy
5.	SQL-Alchemy
6.	Flask-RESTful
7.	Gunicorn and
8.	Pyscopg2 

# Local Development

follow the steps to run app localy in your machine 
1- clone the project 
2 - set database_name and database_path in models.py to the follwing 

    database_name = "Capstone"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)
    
3 - run "flask run" in the command line 



# Authentication:
Currently there are three users created in AUTH0.com :
you can use these token to test the app
### CastingAssistant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3YzY3M2VkYzEwMDNkNjUwMDY2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzAyMTIsImV4cCI6MTU5NzgxNjYxMCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.dgbD_StKSbU3GsL9qHSkkrk1kkUo6R27k3jKiBAnfiyMJOtYx-n9Ebp_4_WpHug6s8_xGs7eR-09ttA_MJT07_p7L0O-sM2WX0GuefC8KDQAVu2LpcKIjDmFc5Sphkt-AdxoWWXcdq0fbTT4AEgnk-wkvW1CZu3lNCyKVmkC7YeG9s6R8MGPZwAtCfscd2_fJ2p3_zQeMs59-I8AicDgdfwtTgIKEp7219Mw6XeeoPq1r_0qPPCgqLccwCT5sNRmBIskBLEmvXShzQf8H0xYfXvWTE2DLRKz5RM5CnwDcettzQuk4osHzOz3_lpAN2pK7_p8l-EAWY3sDDf0R-zZHw


### CastingDirector

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3Zjc2YWE4MDUwMDM3Njg4Mjk3IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzA0ODIsImV4cCI6MTU5NzgxNjg4MCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.TR4tNqHjjD1RbNbgE3TRMmoeMrTsLc11S1t2Zinh--g41ycS2qw8lITaOW6gmwCw4hP4lUTY_3u3H8p9-K21yEQBIivXrmxc9R6wuJMh1CsBmps2f18FpIrEtUQmjbNJGfCenFghVBGXikiUUnBgvn-ybXDnWMVFJ1AiRaYd5ioj5RJtZXtPfn1lVDrP0Rl20zLcf8DuVM1nHjLsoK0GY8q6DQBxRRE-74mC6bth8XlO8QUqIo9AYLSJxr6IMSM3uBiXPF9aNzHtbz8sp4asR_5kHEHJUm2Lw4PhfvZLQ7FwkC0e0c-Zz44NZT8cLOYwAToWkgV2Gn1dL4JsTJReWA

### ExecutiveProducer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M4MTA3M2VkYzEwMDNkNjUwMDk2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc3MzAzNTAsImV4cCI6MTU5NzgxNjc0OCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6bW92aWVzIl19.nKw1E35jUZNWDKvrJuWlwM0JqEE7kj_ubmPfT--fRrZgs5mIhMz0gVlT1JgP8KmZXf-1uUDxhy1WHo8Lv9fjEOgO9zOK_zMcP1OJsdVjaD-YM5obLjdQQVrDo4hAVk6hw_7KVXITXQqatnrrqPcCYI6isazbaKV3lU76hlQagm1KK5xK4VrvIm9DsSuS9Iq6UeblPA0hX2-DmJxwhAMUyNRvx1XLZ5R93PlO4bVja6TGgRmuuGIEcwSrHidXCLFKLpbNj7dsZPr6zZ4B1BHhnvr3-1Q2yEZPhaYk506z4_AXlzmz00eW22ePOO3W5J_IS1Xp2kTZhZhbjK1_mkVqYg


## Endpoint

The url for the API:
https://capstone-final-udacity-project.herokuapp.com/

The endpoints : 


### Movies Endpoint
#### GET '/movies'
    fetches all the movies in the database as json 
    
    https://capstone-final-udacity-project.herokuapp.com/movies
    
##### Example response
```js
{
    "Movies": [
        {
            "id": 2,
            "releaseDate": "2010",
            "title": "title"
        }
    ],
    "success": true
}
```
    

#### POST '/movies'
    create a new movie in the database based on the json that is in the body of the request 
    
    https://capstone-final-udacity-project.herokuapp.com/movies
    
##### Example body
```js
{
    "Movie": 
        {
            "releaseDate": "2010",
            "title": "title"
        }

}
```
##### Example response
```js
{
    "Movies": 
        {
            "id": 2,
            "releaseDate": "2010",
            "title": "title"
        },
    "success": true
}
```

#### DELETE '/movies/delete/movieId'
    This endpoint will delete the movie based on movie ID that is passed 
    

#### PATCH '/movies/int:movie_id'
    This endpoint will modify the movie  based on movie ID that is passed and on the json that is passed into the body of the request 



### Actors Endpoint
#### GET '/actors'
    fetches all the actors in the databse as json 
    
#### POST '/actors'
    This endpoint will create a new actor in the database based on the json that is in the body of the request 
 
#### DELETE '/actors/actorID'
    This endpoint will delete the actor based on actor ID that is passed 

#### PATCH '/actors/actorID' 
    This endpoint will modify the actor based on actor ID that is passed into the url and on the json that is passed into the body of the request 
