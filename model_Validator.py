#model_validator is a Pydantic v2 decorator used to perform validation on the entire model, especially when validation depends on multiple fields rather than a single field.

from pydantic import BaseModel, ValidationError, model_validator
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode='after')  #mode='before' → Raw input dictionary par kaam karna hai. mode='after' → Model object (self) par kaam karna hai.
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self
    
users_data = {
    "password": "Anant@123",
    "confirm_password": "Anant@123"
}

user = User(**users_data)

print(user)