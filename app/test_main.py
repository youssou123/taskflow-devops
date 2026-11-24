from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_list_tasks():
    response = client.post("/tasks", json={"title": "Apprendre Kubernetes"})
    assert response.status_code == 201
    
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()["tasks"]) >= 1