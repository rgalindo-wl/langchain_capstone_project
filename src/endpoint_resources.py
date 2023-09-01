from pydantic import BaseModel


class ResponseIndex(BaseModel):
    response: str
