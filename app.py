from flask import Flask, request, jsonify
from control.control import *
from model.models import db
from utils.utils import *

config = create_config()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:advicehealth@localhost:5431/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.sort_keys = False

db.init_app(app)


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'GET':
        car_amount = request.args.get('car_amount')
        items = CustomerController.get_all(car_amount=car_amount)
        if items is not False:
            return jsonify(items)
        return jsonify({"message": "Something went wrong retrieving customers"}), 400
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        cellphone = request.form.get('cellphone')

        if not name or not name_validator(name=name):
            return jsonify({"message": "The 'name' field is missing or invalid"}), 400
        if not email or not email_validator(email=email):
            return jsonify({'message': "The 'email' field is missing or invalid"}), 400
        if not cellphone or not cellphone_validator(cellphone=cellphone):
            return jsonify({'message': "The 'cellphone' field is missing or invalid"}), 400

        created = CustomerController.create_customer(name=name, email=email, cellphone=cellphone)
        if created:
            return jsonify({'message': 'Customer created successfully'})
        return jsonify({'message': 'Something went wrong creating Customer'}), 500


@app.route('/customer/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def customer_by_id(customer_id):
    if request.method == 'GET':
        result = CustomerController.get_one(id_customer=customer_id)
        if result:
            return jsonify(result)
        return jsonify({'message': 'Customer not found'}), 400
    if request.method == 'PUT':
        name = request.form.get('name')
        email = request.form.get('email')
        cellphone = request.form.get('cellphone')

        if name and not name_validator(name=name):
            return jsonify({"message": "The 'name' field is invalid"}), 400
        if email and not email_validator(email=email):
            return jsonify({'message': "The 'email' field is invalid"}), 400
        if cellphone and not cellphone_validator(cellphone=cellphone):
            return jsonify({'message': "The 'cellphone' field is invalid"}), 400

        result = CustomerController.update_customer(id_customer=customer_id, name=name, email=email,
                                                    cellphone=cellphone)
        if result:
            return jsonify({'message': 'Customer updated sucessfully'})
        return jsonify({'message': 'Customer not found'}), 400

    if request.method == 'DELETE':
        result = CustomerController.delete_customer(id_customer=customer_id)
        if result:
            return jsonify({'message': 'Customer deleted'})
        return jsonify({'message': 'Something went wrong deleting Customer'}), 500


@app.route('/car', methods=['GET', 'POST'])
def car():
    if request.method == 'GET':
        color = request.args.get('color')
        model = request.args.get('model')
        items = CarController.get_all(color=color, model=model)
        if items:
            return jsonify(items)
        return jsonify({"message": "Something went wrong retrieving cars"}), 400

    if request.method == 'POST':
        id_owner = request.form.get('id_owner')
        color = request.form.get('color')
        model = request.form.get('model')

        if not id_owner:
            return jsonify({'message': "id_owner must be informed"}), 400

        if not color_validator(color=color):
            return jsonify({'message': "The 'color' field is missing or invalid."
                                       "It must be 'gray', 'blue' or 'yellow'"}), 400
        if not model_validator(model=model):
            return jsonify({'message': "The 'model' field is missing or invalid."
                                       "It must be 'sedan', 'hatch' or 'convertible'"}), 400

        result, message = CarController.create_car(id_owner=int(id_owner), color=color, model=model)
        if result:
            return jsonify({'message': message})
        return jsonify({'message': message}), 400


@app.route('/car/<int:id_car>', methods=['GET', 'PUT', 'DELETE'])
def car_by_id(id_car):
    if request.method == 'GET':
        result = CarController.get_one(id_car=id_car)
        if result:
            return jsonify(result)
        return jsonify({'message': 'Customer not found'}), 400

    if request.method == 'PUT':
        color = request.form.get('color')
        model = request.form.get('model')

        if color and not color_validator(color=color):
            return jsonify({'message': "The 'color' field is  invalid.It must be 'gray', 'blue' or 'yellow'"}), 400
        if model and not model_validator(model=model):
            return jsonify({'message': "The 'model' field is  invalid."
                                       "It must be 'sedan', 'hatch' or 'convertible'"}), 400

        result = CarController.update_car(id_car=id_car, color=color, model=model)
        if result:
            return jsonify({'message': 'Car updated sucessfully'})
        return jsonify({'message': 'Something went wrong updating Car'}), 400

    if request.method == 'DELETE':
        result = CarController.delete_car(id_car=id_car)
        if result:
            return jsonify({'message': 'Car deleted sucessfully'})
        return jsonify({'message': 'Something went wrong deleting Car'}), 400


with app.app_context():
    print('Creating Database...')
    db.create_all()
    print('All Done!')


def create_app():
    """ Cria instância do flask. """
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    app.run()
