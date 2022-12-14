from typing import List, Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    status: bool = False
    message: str = ""
    code: str = ""
    data: dict = {}

    class Config:
        orm_mode = True


class Contract(BaseModel):
    firstname: str
    lastname: str
    street: str
    zip: int
    city: str
    image: str

    class Config:
        orm_mode = True


class Contracts(ResponseBase):
    data: List[Contract] = []


class SheetURL(BaseModel):
    sheet_url: str


class SheetName(SheetURL):
    sheet_url: str
