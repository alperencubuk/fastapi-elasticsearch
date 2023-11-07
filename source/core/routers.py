from fastapi import APIRouter

from source.app.books.views import books_router

api_router = APIRouter()


api_router.include_router(books_router)
