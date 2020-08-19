# Casting Agency 
This project is the final project for the Udacity Full Stack Developer Nanodegree 

Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Roles
    Casting Assistant:
        Can view actors and movies
    Casting Director:
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies
    Executive Producer:
        All permissions a Casting Director has and…
        Add or delete a movie from the database

# Motivations and Covered Topics

This project is the final project for the Udacity Full Stack Developer Nanodegree.
It covers following topics : 

1. SQL and Data Modeling for the Web 
2. API Development and Documentation
3. Identity and Access Management
4. Deployment on `Heroku`



        
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
#### 1 - clone the project 
#### 2 - set database_name and database_path in models.py to the following 

        database_name = "Capstone"
        database_path = "postgres://{}/{}".format('localhost:5432', database_name)
    
#### 3 - run "flask run" in the command line 



# Authentication:
Currently there are three users created in AUTH0.com :
you can use these token to test the app
### CastingAssistant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3YzY3M2VkYzEwMDNkNjUwMDY2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc4MjQzNDAsImV4cCI6MTU5NzkxMDczOCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.B5HSvvgs_uoBJnuAy3mkkqxFHc5qALc7BDlGZe82HooE1VwKic70DMbjifC3W-keaot-zukheahVBLx_3Tib1ofiUpz-XLFTxnWNYNNDLdZF93pLJVwRAwpNDg6k7AFDZ4Z5IiH0mrDLaqN_fZQHX6xt9fE02jrXEnkiyCfufTDvClqYNZvObGWW8QMHX1-1hRri6FFaWXttkhv5QLNyWrCmcFxIEa9RbvJepBx9bZNEqvbUD3n7Q11ZbT14TerNP9LKODYflccPLjxCWAOO66FFBnFUsWbmPUIc6CSr8qMbWUUAhjp3-JHaygeZtX4m1PkS3zh1aoHStz9IuRL-rw


### CastingDirector

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M3Zjc2YWE4MDUwMDM3Njg4Mjk3IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc4MjQzOTQsImV4cCI6MTU5NzkxMDc5MiwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ejmaDR8J_1xgFClMx-_CZ_ld3q2ccuSHbUQAxJ8C6_DR6NC3t9ysEhAjvus_PSnyiwwdgeFT0OJu9ONxn5WeL9c-3yziYlFF_AHXp2du_fgwCH0hbBdC21S6HM1uieGgag1fT-N7x_LbYWSRsBuCegEebZkGdvR-_E208-whGvYIN_pV4n9UAnihRdfmJfykecYFd9YjwTNt-tPduNVrGHyk7wHiqhCesTn7ysP1WIiIHw9RFzThGX1_h_d3UG3XVW5X_KhJ1OUzYjx6NzAyZEx5yl65iKvUCMF9TrLSF9HCMX_9rfrsbsyDF8LyMvJ8RXzDQ1pHvx_MEm3-gt5Z4A

### ExecutiveProducer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNQTExBUmF0aDZTTFhBUl82N0NhRyJ9.eyJpc3MiOiJodHRwczovL21vYWZhcS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzN2M4MTA3M2VkYzEwMDNkNjUwMDk2IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE1OTc4MjQ0NTAsImV4cCI6MTU5NzkxMDg0OCwiYXpwIjoiZFRITFFNVUhqbHNjc0pQWlFvN1h4dEFTVERLcmNMbFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6bW92aWVzIl19.FgXvtFVtQ2-Klvgx611Fb9Cs3PRqAYgefc0-nFZfjzd9NjxqmFsb5q7wSRLslWs24DZxJ3oC0-PHDFzft48y-zdhbAu-w4FH-_Y4bG_ATdI1WIMdw4cj85_yUaDfzVRR98WlP8anTEhxAebcen9ExsK6hBH-gCEH5B0uYd9ypQBqAEuz1B_gh6thQfxis2PZXagDeMFoxzOJErGEzGJM_L6StgEFbXpTnN1e6Kb4hmPZi4R9_CGY3chtpGsRfu6j1jveP48ouYhIeHHibuG2i55Hz72K9yUNqTJqGhyHpv-5OKvfv5T1RtlXi00V338lfgSvyJBqZz3WMIP-OOo_cw


## Endpoint

The url for the API:
https://capstone-final-udacity-project.herokuapp.com/

The endpoints : 


### Movies Endpoint
#### GET '/movies'
    fetches all the movies in the database as json 

    
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
    
##### Example response
```js     
{
    "delete": 2,
    "success": true
}
``` 

#### PATCH '/movies/int:movie_id'
    This endpoint will modify the movie  based on movie ID that is passed and on the json that is passed into the body of the request 
##### Example body 
```js  
{
    "releaseDate": "2010",
    "title": "updated title"
}
```
##### Example response 
```js  
{
    "Movies": {
        "id": 6,
        "releaseDate": "2010",
        "title": "updated title"
    },
    "success": true
}
```

### Actors Endpoint
#### GET '/actors'
    fetches all the actors in the databse as json 
    
##### Example response 
```js     
{
    "actors": [
        {
            "age": 21,
            "gender": "male",
            "id": 2,
            "name": "moafaq"
        }
    ],
    "success": true
}
```
    
#### POST '/actors'
    This endpoint will create a new actor in the database based on the json that is in the body of the request
##### Example body 
```js  
{
    "age": 21,
    "gender": "male",
    "name": "moafaq"
}
```
##### Example response 
```js  
{
    "Actors": {
        "age": 21,
        "gender": null,
        "id": 3,
        "name": "moafaq"
    },
    "success": true
}
```
#### DELETE '/actors/actorID'
    This endpoint will delete the actor based on actor ID that is passed 
##### Example response 
```js  
{
    "delete": 3,
    "success": true
}
```
#### PATCH '/actors/actorID' 
    This endpoint will modify the actor based on actor ID that is passed into the url and on the json that is passed into the body of the request 
##### Example body 
```js     
{
    "age": 21,
    "gender": "male",
    "name": "updated name"
}
```
##### Example response 
```js     
{
    "Actors": {
        "age": 21,
        "gender": "male",
        "id": 2,
        "name": "updated name"
    },
    "success": true
}
```
