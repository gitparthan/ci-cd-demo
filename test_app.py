
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_api(client):
    response = client.post(
        "/api/add",
        json={"a": 10, "b": 20}
    )
    assert response.status_code == 200
    assert response.json["result"] == 30

def test_invalid_input(client):
    response = client.post(
        "/api/add",
        json={"a": "abc", "b": 20}
    )
    assert response.status_code == 400
