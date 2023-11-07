from pydantic import BaseModel


class Book(BaseModel):
    title: str
    detail: str


class BookSearch(BaseModel):
    query: str
    fields: str = "title, detail"
