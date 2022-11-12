import pytest

from app.app import create_app, app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def response_customers(client):

    response = client.get('/customer')
    return response

@pytest.fixture
def response_fail_customer_name(client):
    data = {
        'name': '123',
        'email': 'teste@silva.com',
        'cellphone': '11222223333'
    }
    response = client.post('/customer', data=data)
    return response

@pytest.fixture
def response_fail_customer_email(client):
    data = {
        'name': 'teste da silva',
        'email': 'teste-silva.com',
        'cellphone': '11222223333'
    }
    response = client.post('/customer', data=data)
    return response

@pytest.fixture
def response_fail_customer_cellphone(client):
    data = {
        'name': 'teste da silva',
        'email': 'teste@silva.com',
        'cellphone': 'xx'
    }
    response = client.post('/customer', data=data)
    return response

