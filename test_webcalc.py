import pytest
from expecter import expect

from webcalc import app


@pytest.fixture
def client():
    return app.test_client()

def describe_index():

    def it_says_hello(client):
        response = client.get('/')

        expect(response.data).contains(b"Hello, Aaron!")

def describe I DONT KNOW WHAT I AM DOING _calc():
    def when_plus(client):
        response = client.get('/4/+/5')
        expect(response.data).contains(b"9")