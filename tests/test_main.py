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
        "id": 12345,
        "name": "Yamada",
    }
    
# ユーザー情報取得API 異常系テスト
# トークン違い
def test_get_user_ABR001():
    response = client.get("/users/abcde12345",
                          headers={"token": "dummy_token"})
    assert response.status_code == 400
    assert response.json() == {"detail": "token_verification_failed"}

# ユーザー情報取得API 異常系テスト
# 存在しないユーザー指定
def test_get_user_ABR002():
    response = client.get(
        "/users/hogefuga", headers={"token": "correct_token"})
    assert response.status_code == 404
    assert response.json() == {"detail": "user_not_found"}