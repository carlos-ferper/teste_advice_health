# Advice Health Teste

this project emulates the system of a shop that sells cars to residents of the city of Nork-Town. In this system it is possible to create customers and add cars to them, with a maximum limit of 3 cars per customer. Cars have two conditions: the color must be 'yellow', 'grey' or 'blue', the model must be 'hatch', 'sedan' or 'convertible'.

## 🛢️ Data modelling

### Customer

Model the customer of CarFord Store

Fields:

**name** - refers to costumer’s name

**email** -refers to custumer’s email (it is validated by regex on creation)

**cellphone** - refers to customer’s cellphone (it should have at least 10 digits and a limit of 14 digits)

### Car

Model cars selled to customers at CarFord. All cars must have a owner and each owner can have up to 3 cars only.

Fields:

**id_owner** - refers to customer's I'd that owns the car

**color** - refers to car's color. It's limited to some possibilities: 'blue', 'gray' or 'yellow'

**model** - refers to car's model. It's limited to some possibilities: 'hatch', 'sedan' or 'convertible'


## 🚧 Dependencies

If you want to run this application, you will need 

###  database
Postgres 12.1 at least

### pytohn version
Python 3.8.5

### libs and frameworks

All the libs and frameworks used can be found at `requirements.txt`

## 🏠 Run application on my own server

It's necessary to install dependencies first

`pip install requirements.txt`

Then, you should run a SQL file to create the database

`create_db.sql`

To run application, use the following command

flask -m run host=’’0.0.0.0”


## 🚢 Docker compose

If you want to only run the application, it’s possible to use docker-compose file. It has all necessary dependencies and features used in the project

`docker-compose build`

Then, to use the system, access:

` localhost:5000 `



## 🛣️ Routes

### GET /customer

Return all customers 

### POST/customer

Create a new customer 

Input body
```
{ ‘’name”: <customer_name>, 

“email” : <customer_email> (must be valid)

“cellphone”: <customer_crllhpone> (must be valid, containing only numbers and has length between 10 and 14)

}
```

### GET/customer/<id:int>

Return customer with that id

### PUT /customer/<id: int>

Updates customer with that id

### DELETE  /customer/<id: int>

Deletes customer with that id

### GET /car

Return all cars, it's possible to filter by color and model.

`GET /car?color=&model=`

### POST /car

Creates a new car

Input body

```
{ ‘’id_owner”: <customer’s Id>,

“color”: <car_color> [blue|gray|yellow],

“model”: <car_model> [hatch|sedan|convertible]

}
```

### GET /car/<id:int>

Return car within that id

### PUT  /car/<id:int>

Updates car within that id

### DELETE  /car/<id:int>

Deletes car with that id


## 🛠️ Made With


* [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask Framework
* [Flask-SQLAchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/#) - ORM

## ✒️ Authors

* **Carlos Vinicius Fernandes Pereira** - [Linkedin](https://www.linkedin.com/in/carlos-vinicius-fernandes-pereira-981747140/)
