import pytest
from app import app
#Functional Testing of my application through a sonar cloud quality gate. 
@pytest.fixture
def client(): #Set's up the client for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200 # Tests if HTTP Response is OK by being a 200 Response
    print(rv.data)  # Debug print statement to inspect the response content
    #assert b'APPLICATION-A' in rv.data or b'APPLICATION-B' in rv.data  # Updated to match the application content
    assert b'Counter Value' in rv.data 

def test_increment(client):
    rv = client.post('/increment')
    assert rv.status_code == 200
    assert b'counter' in rv.data 



# Dynamic Functional Testing is invoked to Confirm http connection is valid and specified assertions are met and located in the file.
