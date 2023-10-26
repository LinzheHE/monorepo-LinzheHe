import json
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_path():
    response = client.get("/books/BookTitle")
    assert response.status_code == 200
    assert response.json() == {"Book Title": "BookTitle"}

def test_read_query():
    response = client.get("/books/?author=JK%20Rowling")
    assert response.status_code == 200
    assert response.json() == {"Book Author": "JK Rowling"}

def test_read_path_and_query():
    response = client.get("/books/Harry%20Potter/?author=Rowling")
    assert response.status_code == 200
    assert response.json() == {"Book Title": "Harry Potter", "Author": "Rowling"}

def test_create_book():
    book_data = {
        "name": "New Book",
        "author": "New Author"
    }
    response = client.post("/books/create_book/", json=book_data)
    assert response.status_code == 200
    assert "book_id" in response.json()
    assert "new book" in response.json()

def test_update_book():
    book_data = {
        "name": "Updated Book Name",
        "author": "Updated Author Name"
    }
    response = client.put("/books/update_book/1", json=book_data)  
    assert response.status_code == 200
    assert "book_id" in response.json()
    assert "updated_data" in response.json()

def test_update_book_not_found():
    book_data = {
        "name": "Updated Book Name",
        "author": "Updated Author Name"
    }
    response = client.put("/books/update_book/99", json=book_data)  
    assert response.status_code == 200
    assert "error" in response.json()

def test_delete_book():
    response = client.delete("/books/delete_book/1")
    assert response.status_code == 200
    assert "message" in response.json()

def test_delete_book_not_found():
    response = client.delete("/books/delete_book/99")
    assert response.status_code == 200
    assert "error" in response.json()