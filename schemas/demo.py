from pydantic import BaseModel
from typing import List
from typing import Optional


class User(BaseModel):
    name: str
    email: str        
    password: str
    contact_no : int

class ShowUser(BaseModel):
    name: str
    email_id : str   
    contact_no : int

class Login(BaseModel):
    email : str
    password : str

class ResponseCommonMessage(BaseModel):
    status: str
    message: str