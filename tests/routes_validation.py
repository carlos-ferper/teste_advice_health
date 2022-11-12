import pytest
from app.app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_route_get_all_customers(client, response_customers):
    assert response_customers.status_code == 200


def test_fail_create_customer_name(client, response_fail_customer_name):
    assert response_fail_customer_name.status_code == 400


def test_fail_create_customer_email(client, response_fail_customer_email):
    assert response_fail_customer_email.status_code == 400


def test_fail_create_customer_cellphone(client, response_fail_customer_cellphone):
    assert response_fail_customer_cellphone.status_code == 400


