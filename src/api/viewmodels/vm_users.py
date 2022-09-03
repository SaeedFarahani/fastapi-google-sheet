from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import Form

class vm_response_base(BaseModel):
    status: bool = False
    message: str = ""
    code: str = ""
    data: dict = None

    class Config:
        orm_mode = True

class vm_di_checkapi(BaseModel):
    api: str

    class Config:
        orm_mode = True

class vm_di_user(BaseModel): # view model data item user
    id: Optional[int]
    username: str
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    age: str
    nid: str
    image: Optional[str] = ""

    class Config:
        orm_mode = True

class Users(BaseModel):
    id: Optional[int]
    username: str
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    age: str
    nid: str
    image: Optional[str] = ""

    class Config:
        orm_mode = True

class vm_user(BaseModel):
    username: str
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    age: str
    nid: str
    image: str = Form("")

    class Config:
        orm_mode = True

class vm_user_update(BaseModel):
    username: str
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    age: str
    nid: str
    image: Optional[str]= Form(...)

    class Config:
        orm_mode = True

class vm_username(BaseModel):
    status: bool
    message: str
    code: str
    username: str

    class Config:
        orm_mode = True


class vm_response(BaseModel):
    status: bool
    message: str
    code: str
    data: dict = None

    class Config:
        orm_mode = True


class vm_response_data(vm_response):
    data: dict

    class Config:
        orm_mode = True

class vm_user_validdays(BaseModel):
    username: str
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    age: str
    nid: str
    image: Optional[str] = ""

    class Config:
        orm_mode = True

class vm_up(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
