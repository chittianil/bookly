
from pydantic import BaseModel


class Book(BaseModel):
       id:  int
       title: str
       author: str
       genre: str
       published_year: int
       price: float

class BookUpdateModel(BaseModel):
       title: str
       author: str
       publisher: str
       pagecount: int
       language:str