# from decouple import config
import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "customer"
    __table_args__ = {"schema": "carford"}

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
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'cellphone_number': self.cellphone_number,
            'car_number': self.car_number
        }


    @staticmethod
    def get(id: int = None):
        if id:
            return Customer.query.filter(Customer.id == id).first()
        return Customer.query.all()


class EnumColor(enum.Enum):
    yellow = "yellow"
    blue = "blue"
    gray = "gray"


class EnumModel(enum.Enum):
    hatch = "hatch"
    sedan = "sedan"
    convertible = "convertible"


class Car(db.Model):
    __tablename__ = "car"
    __table_args__ = {"schema": "carford"}

    id = db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer, db.ForeignKey('carford.customer.id'))
    model = db.Column(Enum(EnumModel))
    color = db.Column(Enum(EnumColor))
    owner = relationship('Customer')

    def __init__(self, owner: Customer, model, color):
        self.owner = owner
        self.id_owner = owner.id
        self.model = model
        self.color = color

        self.owner.car_number += 1

    def delete_car(self):
        self.owner.car_number -= 1

    def __repr__(self):
        return {
            'id': self.id,
            'id_owner': self.id_owner,
            'model': self.model.value,
            'color': self.color.value,
        }

    @staticmethod
    def get(id: int = None):
        if id:
            return Car.query.filter(Car.id == id).first()
        return Car.query.all()

    @staticmethod
    def get_by_owner_id(id: int):
        return Car.query.filter(Car.id_owner == id).first()
