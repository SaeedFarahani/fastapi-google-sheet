from typing import List, Optional

from pydantic import BaseModel


class Contract(BaseModel):
    firstname: str
    lastname: str
    street: str
    zip: int
    city: str
    image: str

    class Config:
        orm_mode = True


class Contracts:
    data: List[Contract]
