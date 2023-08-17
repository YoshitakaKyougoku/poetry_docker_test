from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
    
def test_users():
    response = client.post(
        "/users",
        headers = {"users": "User"},
        json = {"user_id": 55678, "user_name": "京極慶高"})
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 55678,
        "user_name": "京極慶高",
    }