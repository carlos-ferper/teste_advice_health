from flask import Flask, request, jsonify
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    # TODO: remover esse create all daqui e colocar em algum outro lugar
    db.create_all()
    if request.method == 'GET':
        items = [customer.__repr__() for customer in Customer.get()]
        return jsonify(items)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cellphone = request.form['cellphone']

        customer = Customer(name=name, email=email, cellphone_number=cellphone)
        db.session.add(customer)
        db.session.commit()
        return 'sucesso'


@app.route('/customer/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def customer_by_id(id):
    if request.method == 'GET':
        items = Customer.get(id)
        return jsonify(items.__repr__())
    if request.method == 'PUT':
        name = request.form.get('name')
        email = request.form.get('email')
        cellphone = request.form.get('cellphone')

        customer = Customer.get(id)
        customer.name = name if name else customer.name
        customer.email = email if email else customer.email
        customer.cellphone_number = cellphone if cellphone else customer.cellphone_number
        db.session.add(customer)
        db.session.commit()
        return 'sucesso'

    if request.method == 'DELETE':
        customer = Customer.get(id)
        db.session.delete(customer)
        db.session.commit()

        return 'sucesso'


@app.route('/customer_cars/<int:id>', methods=['GET'])
def customer_cars(id):
    items = [car.__repr__() for car in Car.get_by_owner_id(id)]
    return jsonify(items.__repr__())


@app.route('/car', methods=['GET', 'POST'])
def car():
    if request.method == 'GET':
        items = [car.__repr__() for car in Car.get()]
        return jsonify(items)

    if request.method == 'POST':
        id_owner = int(request.form['id_owner'])
        color = request.form['color']
        model = request.form['model']

        owner = Customer.get(id_owner)
        car = Car(owner=owner, color=color, model=model)
        db.session.add(car)
        db.session.commit()
        return 'sucesso'


@app.route('/car/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def car_by_id(id):
    if request.method == 'GET':
        items = Car.get(id)
        return jsonify(items.__repr__())

    if request.method == 'PUT':
        color = request.form['color']

        car = Car.get(id)
        car.color = color if color else car.color
        db.session.add(car)
        db.session.commit()
        return 'sucesso'

    if request.method == 'DELETE':
        car = Car.get(id)
        car.delete_car()
        db.session.delete(car)
        db.session.commit()

        return 'sucesso'


if __name__ == '__main__':
    app.run()
