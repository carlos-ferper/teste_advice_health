import enum
from utils.utils import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

db = SQLAlchemy()

config = create_config()

class Customer(db.Model):
    __tablename__ = "customer"
    __table_args__ = {"schema": 'carford'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    cellphone = db.Column(db.String())
    car_amount = db.Column(db.Integer())

    def __init__(self, name, email, cellphone):
        self.name = name
        self.email = email
        self.cellphone = cellphone
        self.car_amount = 0
        self.car_list = []

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'cellphone_number': self.cellphone,
            'car_amount': self.car_amount,
            'car_list': [car.__repr__() for car in self.car_list]
        }


    @staticmethod
    def get(customer_id: int = None, car_amount: int = None) -> list:
        filtros = []
        if customer_id:
            filtros.append(Customer.id == customer_id)
        if car_amount:
            filtros.append(Customer.car_amount == car_amount)
        customer_list = Customer.query.filter(*filtros).all()
        for customer in customer_list:
            car_list = Car.get_by_owner_id(customer.id)
            customer.car_list = car_list

        return customer_list


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
    __table_args__ = {"schema": 'carford'}

    id = db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer, db.ForeignKey('carford.customer.id'))
    model = db.Column(Enum(EnumModel, schema='carford'), )
    color = db.Column(Enum(EnumColor, schema='carford'))
    owner = relationship('Customer')

    def __init__(self, owner: Customer, model, color):
        self.owner = owner
        self.id_owner = owner.id
        self.model = model
        self.color = color

        self.owner.car_amount += 1
        self.owner.car_list.append(self)

    def __repr__(self):
        return {
            'id': self.id,
            'id_owner': self.id_owner,
            'model': self.model.value,
            'color': self.color.value,
        }

    @staticmethod
    def get(id_car: int = None, color: str = None, model: str = None) -> list:
        filtros = []
        if color:
            filtros.append(Car.color == color)
        if model:
            filtros.append(Car.model == model)
        if id_car:
            filtros.append(Car.id == id_car)
        car_list = Car.query.filter(*filtros).all()
        for car in car_list:
            car.owner = Customer.get(customer_id=car.id_owner)[0]
        return car_list

    @staticmethod
    def get_by_owner_id(id_owner: int) -> list:
        return Car.query.filter(Car.id_owner == id_owner).all()
