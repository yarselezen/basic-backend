# basic-backend
The project represents a simple server app with an embedded database providing an example of REST API for Create and Read operations

## Technologies
### Frameworks  
- [Bottle](https://bottlepy.org/docs/dev/) is used as an HTTP server framework
### Libraries
- [CuttlePool](https://pypi.org/project/cuttlepool/) is an implementation of a database connection pool
### Database 
[SQLite](https://www.sqlite.org/index.html)

## Before you start
Make sure you have [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/quickstart/) installed  

## Starting server
Execute the following command from the command line:  
```sh
~ python main.py
```  
The server will start on 127.0.0.1:8080  
  
To choose another port you can pass it as a command line argument:  
```sh
~ python main.py 5000
```  
The server will start on 127.0.0.1:5000  
  
To run server on 0.0.0.0 pass the host and a port:  
```sh
~ python main.py 0.0.0.0 5000
```  
## Before you start in Docker
Make sure you have [Docker](https://www.docker.com/) installed  
## Starting server in Docker
The repository contains [Dockerfile](https://github.com/kisliakovsky/basic-backend/blob/main/Dockerfile).  
To start the server in Docker you should [build a Docker image from the Dockerfile](https://docs.docker.com/language/python/build-images/#build-an-image):  
```sh
~ docker build --tag basic-backend .
```
And run the image as a Docker container:  
```sh
~ docker run --publish 127.0.0.1:5000:5000 basic-backend
```
The server will start on 127.0.0.1:5000

## Server API
#### Say hello
Greets the user
##### Request
```
GET /
```
##### Response
**Status**
200
**Body**
```
Hello!
```
### User API
#### Get users
Returns the list of users
##### Request
```
GET /users
```
##### Response
**Status**
200
**Body schema**
```js
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "first_name": {
        "description": "The first name of the user",
        "type": "string"
      },
      "last_name": {
        "description": "The last name of the user",
        "type": "string"
      },
      "phone": {
        "description": "The phone of the user",
        "type": "string"
      }
    }
  }
}
```
**Body example**
```js
[
  {
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "phone": "+79111111111"
  },
  {
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+449111111111"
  },
  {
    "first_name": "Johann",
    "last_name": "Schmidt",
    "phone": "+499111111111"
  }
]
```
#### Create a user
Creates a new user
##### Request
```
POST /users
```
**Body schema**
```js
{
  "type": "object",
  "properties": {
    "first_name": {
      "description": "The first name of the user",
      "type": "string"
    },
    "last_name": {
      "description": "The last name of the user",
      "type": "string"
    },
    "phone": {
      "description": "The phone of the user",
      "type": "string"
    }
  }
}
```
**Body example**
```js
{
    "first_name": "Oleg",
    "last_name": "Petrov",
    "phone": "+79850000000"
}
```
##### Response
**Status**
201
