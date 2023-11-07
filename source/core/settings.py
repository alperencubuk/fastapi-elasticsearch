from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "FastAPI Elasticsearch"
    VERSION: str = "1.0.0"

    ELASTICSEARCH_HOST: str = "elasticsearch"
    ELASTICSEARCH_PORT: int = 9200
    ELASTICSEARCH_SCHEME: str = "http"
    ELASTICSEARCH_URI: str | None = None

    BOOK_INDEX: str = "books"

    @model_validator(mode="after")
    def validator(cls, values: "Settings") -> "Settings":
        values.ELASTICSEARCH_URI = (
            f"{values.ELASTICSEARCH_SCHEME}://"
            f"{values.ELASTICSEARCH_HOST}:"
            f"{values.ELASTICSEARCH_PORT}"
        )
        return values


def get_settings():
    return Settings()


settings = get_settings()
