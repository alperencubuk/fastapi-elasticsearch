from fastapi import APIRouter, Depends, HTTPException, status

from source.app.books.schemas import Book, BookSearch
from source.app.books.services import add_book, search_book
from source.core.schemas import ExceptionSchema

books_router = APIRouter(prefix="/books")


@books_router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    tags=["books"],
)
async def book_add(book: Book) -> Book:
    if new_book := await add_book(book=book):
        return new_book
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Elasticsearch error.",
    )


@books_router.get(
    "/",
    response_model=list[Book],
    responses={status.HTTP_404_NOT_FOUND: {"model": ExceptionSchema}},
    tags=["books"],
)
async def book_search(query: BookSearch = Depends()) -> list:
    if book := await search_book(query=query):
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Query does not match any of books.",
    )
