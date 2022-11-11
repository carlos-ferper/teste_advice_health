# from decouple import config
from flask_sqlalchemy import SQLAlchemy, Enum

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    cellphone_number = db.Column(db.String())
    car_number = db.Column(db.Integer())

    def __init__(self, name, email, cellphone_number):
        self.name = name
        self.email = email
        self.cellphone_number = cellphone_number
        self.car_number = 0

    def __repr__(self):
        return f"{self.name}:{self.email}"


class Car(db.Model):
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer, db.ForeignKey('customer.id'))
    model = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, owner: Customer, model, color):
        self.owner = owner
        self.id_owner = owner.id
        self.model = model
        self.color = color

        self.owner.car_number += 1

    def __repr__(self):
        return f"{self.id_owner}:{self.model} - {self.color}"
