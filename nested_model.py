from pydantic import BaseModel, Field, EmailStr, conint, constr
from fastapi import FastAPI
app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    username: str
    email: EmailStr
    age: conint(gt=0)
    address: Address

user_data = {
    "username": "Anant_Awasthi",
    "email": "anantawasthi773@gmail.com",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Lucknow",
        "state": "UP",
        "zip_code": "226001"
    }
}

user = User(**user_data)
print(user)