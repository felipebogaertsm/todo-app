from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_todo_read_all():
    response = client.get("/todos")
    assert response.status_code != 200
