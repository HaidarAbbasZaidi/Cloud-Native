
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_task():
    client = app.test_client()
    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"}
    )
    assert response.status_code == 201
    assert response.json["title"] == "Learn Docker"
