import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'APPLICATION-2' in rv.data
    assert b'Counter Value' in rv.data

def test_increment(client):
    rv = client.post('/increment')
    assert rv.status_code == 200
    assert b'counter' in rv.data