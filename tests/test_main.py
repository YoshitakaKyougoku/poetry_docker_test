from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
    
def test_get_user_NR001():
    response = client.get(
        "/users/abcde12345", headers={"token": "correct_token"})
    # レスポンス検証
    # ステータスコード
    assert response.status_code == 200
    # レスポンスボディ
    assert response.json() == {
        "id": "abcde12345",
        "name": "Yamada",
        "email_address": "yamada@example.com",
    }