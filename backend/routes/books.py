from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Book
from schema import BookSchema
from supabase_client import supabase

router = APIRouter()

"""
Query all books
"""
@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    """
    Get all books from the database.
    """
    try:
        books = supabase.table("books").select("*").execute()
        return books.data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching books from Supabase")

"""
Query a single book by ID
"""
@router.get("/books/{book_id}")
def get_books_by_id(book_id: str, db:Session = Depends(get_db)):
    """
    Get a book by its ID.
    """
    try:
        book = supabase.table("books").select("*").eq("book_id", book_id).single().execute()
        if not book.data:
            raise HTTPException(status_code=404, detail="Book not found")
        return book.data
    except Exception as e:
        print("Error fetching book: ", e)
        raise HTTPException(status_code=500, detail="Error fetching book from Supabase")

@router.post("/books")
def create_book(book: BookSchema):
    try:
        response = supabase.table("books").insert(book.dict()).execute()
        return response.data
    except Exception as e:
        print("❌ Insert error:", e)
        raise HTTPException(status_code=500, detail="Could not insert book")

    print("Book inserted successfully!")


"""
Query a single book by author
"""
# @router.get("/books/{author_name}")


"""
Query a single book by title
"""
# @router.get("/books/{title}")


"""
Query all books by year
"""
# @router.get("/books/{year_published}")


"""
Query all books by genre
"""
# @router.get("/books/genre")