from pydantic import BaseModel


class ExceptionSchema(BaseModel):
    detail: str


class HealthSchema(BaseModel):
    api: bool
    elasticsearch: bool
