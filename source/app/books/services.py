import logging

from source.app.books.schemas import Book, BookSearch
from source.core.elasticsearch import es
from source.core.settings import settings

logger = logging.getLogger(__name__)


async def add_book(book: Book) -> Book | None:
    try:
        es.index(index=settings.BOOK_INDEX, body=book.model_dump())
        return book
    except Exception as error:
        logger.error(
            f"[ERROR] [ADD] Detail: {error}",
        )
        return None


async def search_book(query: BookSearch) -> list:
    search_query = {
        "multi_match": {
            "query": query.query,
            "fields": [field.strip() for field in query.fields.split(",")],
        }
    }

    try:
        response = es.search(index=settings.BOOK_INDEX, query=search_query)
        result = []
        for hit in response["hits"]["hits"]:
            result.append(hit["_source"])
        return result
    except Exception as error:
        logger.error(
            f"[ERROR] [SEARCH] Detail: {error}",
        )
        return []
