from pydantic import BaseModel, ValidationError, field_validator
from fastapi import FastAPI


app = FastAPI()
class User(BaseModel):
    username : str
    password : str
    Gender : str
    age: int

    @field_validator('age')
    @classmethod
    def age_must_be_positive(cls, value):  #cls = class method ; value are those values which are passed to the age field (age=25)
        if value <= 0:
            raise ValueError('Age must be a positive integer')
        return value
    

    
# user = User(
#     username="Anant_Awasthi",
#     password="Anant@123",
#     Gender="Male",
#     age=25
# )

#print(user)

#Python Dictionary (Most Common/ Real world)

user_data = {
    "username": "Anant_Awasthi",
    "password": "Anant@123",
    "Gender": "Male",
    "age": 25
}

user = User(**user_data)

print(user)

