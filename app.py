from flask import Flask

app = Flask(__name__)


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    pass


@app.route('/customer/<int:id>', methods=['GET', 'POST', 'DELETE'])
def customer_by_id(id):
    pass


@app.route('/car', methods=['GET', 'POST'])
def car():
    pass


@app.route('/car/<int:id>', methods=['GET', 'POST', 'DELETE'])
def car_by_id(id):
    pass


if __name__ == '__main__':
    app.run()
