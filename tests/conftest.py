import pytest
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from app import app

@pytest.fixture()
def app():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_example(client):
    response = client.get("/")
    assert b"<h2>Hello, World!</h2>" in response.data
    
def test_json_data(client):
    response = client.post("/auth", json={
    "email":"superadmin@gmail.com",
    "password":"superadmin"
    })
    assert response.json["data"]["token"] is not None
    
def test_get_contact(client):
    response = client.get("/contact")
    assert response.status_code == 200