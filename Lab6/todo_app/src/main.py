from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# --------------------- Create a GET ReST API --------------------- #
@app.get("/api")
def read_root():
    return {"msg": "Hello World"}


# --------------------- Create a GET ReST API with path parameters --------------------- #
@app.get("/books/{book_title}")
def read_path(book_title: str):
    return {"Book Title": book_title}


# --------------------- Create a GET ReST API with query parameters --------------------- #
@app.get("/books/")
def read_query(author: str):
    return {"Book Author": author}


# --------------------- Create a GET ReST API with path parameters AND query parameters --------------------- #
@app.get("/books/{book_title}/")
def read_path(book_title: str, author: str):
    return {"Book Title": book_title, "Author": author}


# --------------------- Create a POST ReST API --------------------- #
# Simulate an in-memory database
books = {}
# create a pydantic model to define the request body structure
class Book(BaseModel):
    name: str
    author: str
    
@app.post("/books/create_book/")
def create_book(new_book: Book):
    book_id = len(books) + 1
    books[book_id] = new_book
    return {"book_id": book_id, "new book": new_book}


# --------------------- Create a PUT ReST API --------------------- #
# create a pydantic model to define the request body structure for updates
class UpdateBook(BaseModel):
    name: str
    author: str

@app.put("/books/update_book/{book_id}")
def update_book(book_id: int, book_data: UpdateBook):
    if book_id in books:
        # Update the book with the new data
        books[book_id] = book_data
        return {"book_id": book_id, "updated_data": book_data}
    else:
        return {"error": "Book not found"}


# --------------------- Create a DELETE ReST API --------------------- #
# Create a Pydantic model to define the request parameters
class DeleteRequest(BaseModel):
    book_id: int

@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    if book_id in books:
        # Remove the book from the database
        del books[book_id]
        return {"message": f"Book with ID {book_id} has been deleted."}
    else:
        return {"error": "Book not found"}