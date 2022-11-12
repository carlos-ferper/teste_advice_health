from model.models import *


class CustomerController:

    @staticmethod
    def get_all(car_amount: int = None) -> list or bool:
        """
        Get all customers, it is possible to filter by car amount
        :param car_amount: amount of cars to filter
        :return: list of customers
        """
        try:
            customer_list = Customer.get(car_amount=car_amount)
            return [customer.__repr__() for customer in customer_list]
        except:
            return False

    @staticmethod
    def get_one(id_customer: int) -> dict or None:
        """
        Get customer by it database id
        :param id_customer: customer id on database
        :return: equivalent Customer of that id or None
        """
        try:
            query_result = Customer.get(customer_id=id_customer)
            if query_result and len(query_result) == 1:

                return query_result[0].__repr__()
            return None
        except:
            return None

    @staticmethod
    def create_customer(name: str, email: str, cellphone: str) -> bool:
        """
        Create a new Customer in database
        :param name: customer name (must be valid, not containing numbers)
        :param email: customer email (must be valid, containing @ and a domain)
        :param cellphone: customer cellphone (only numbers)
        :return: created, message
        """
        try:
            new_customer = Customer(name=name, email=email, cellphone=cellphone)
            db.session.add(new_customer)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def update_customer(id_customer: int, name: str = None, email: str = None, cellphone: str = None) -> bool:
        """
        Update a customer registry
        :param id_customer: customer id to be updated
        :param name: customer new name
        :param email: customer new email
        :param cellphone: customer new cellphone
        :return: if update worked
        """
        customer = Customer.get(customer_id=id_customer)
        if customer and len(customer) == 1:
            try:
                customer = customer[0]
                customer.name = name if name else customer.name
                customer.email = email if email else customer.email
                customer.cellphone = cellphone if cellphone else customer.cellphone
                db.session.add(customer)
                db.session.commit()

                return True
            except:
                return False
        return False

    @staticmethod
    def delete_customer(id_customer: int) -> bool:
        """
        Delete a customer from database
        :param id_customer: customer's id on database
        :return: if the deletion occurred successfully
        """
        customer = Customer.get(id_customer)
        if customer:
            customer = customer[0]
            try:
                car_list = customer.car_list
                for car in car_list:
                    db.session.delete(car)
                db.session.delete(customer)
                db.session.commit()
                return True
            except:
                return False
        return False


class CarController:

    @staticmethod
    def get_all(color: str = None, model: str = None) -> list or bool:
        """
        Get all cars, it is possible to filter by color and/or model
        :param color: filter by car color
        :param model: filter by car model
        :return: list of cars that matches the filters
        """
        try:
            car_list = Car.get(color=color, model=model)
            return [car.__repr__() for car in car_list]
        except:
            return False

    @staticmethod
    def get_one(id_car: int) -> dict or None:
        """
        Get car by id
        :param id_car: car id on database
        :return: car json representation or None if not found
        """
        try:
            query_result = Car.get(id_car=id_car)
            if query_result and len(query_result) == 1:
                return query_result[0].__repr__()
            return None
        except:
            return None

    @staticmethod
    def create_car(id_owner: int, color: str, model: str) -> (bool, str):
        """
        Create a new car. An owner can't have mora than 3 cars, so there is a validation on code to do this
        :param id_owner: car must be associated with a owner
        :param color: car color, must be in ['yellow', 'gray', 'blue']
        :param model: car model, must be ['hatch', 'sedan', 'convertible']
        :return: if the operation occurred successfully and if something doesn't work, the motivation
        """
        owner_result = Customer.get(customer_id=id_owner)
        if owner_result and len(owner_result) == 1:
            owner = owner_result[0]
            if owner.car_amount < 3:
                try:
                    car = Car(owner=owner, color=color, model=model)
                    db.session.add(car)
                    db.session.commit()
                    return True, 'Car created sucessfully'
                except:
                    return False, 'Something went wrong creating Car'
            return False, 'Customer already has reached the car amount limit'
        return False, 'Customer not found'

    @staticmethod
    def update_car(id_car: int, color: str = None, model: str = None) -> bool:
        """
        Update car information
        :param id_car: car id to be updated
        :param color: car new color
        :param model: car new model
        :return: if all changes worked
        """

        query_result = Car.get(id_car=id_car)
        if query_result and len(query_result) == 1:
            car = query_result[0]
            try:
                car.color = color if color else car.color
                car.model = model if model else car.model
                db.session.add(car)
                db.session.commit()
                return True
            except:
                return False
        return False

    @staticmethod
    def delete_car(id_car: int) -> bool:
        """
        delete a car
        :param id_car: car id to be deleted
        :return: if operation worked
        """
        query_result = Car.get(id_car=id_car)
        if query_result and len(query_result) == 1:
            car = query_result[0]
            try:
                car.owner.car_amount -= 1
                db.session.add(car.owner)
                db.session.delete(car)
                db.session.commit()
                return True
            except:
                return False
        return False

