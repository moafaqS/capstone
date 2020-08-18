# capstone
This project is the final project for the Udacity Full Stack Developer Nanodegree 


# Endpoint

The url for the API:
https://capstone-final-udacity-project.herokuapp.com/

The endpoints : 


## Movies Endpoint
GET '/movies'
    fetches all the movies in the database as json 

POST '/movies'
    create a new movie in the database based on the json that is in the body of the request 

DELETE '/movies/delete/movieId'
    This endpoint will delete the movie based on movie ID that is passed 
    

PATCH '/movies/int:movie_id'
    This endpoint will modify the movie  based on movie ID that is passed and on the json that is passed into the body of the request 



## Actors Endpoint
GET '/actors'
    fetches all the actors in the databse as json 
    
POST '/actors'
    This endpoint will create a new actor in the database based on the json that is in the body of the request 
 
DELETE '/actors/actorID'
    This endpoint will delete the actor based on actor ID that is passed 

PATCH '/actors/actorID' 
    This endpoint will modify the actor based on actor ID that is passed into the url and on the json that is passed into the body of the request 
