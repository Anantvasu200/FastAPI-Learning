from pydantic import BaseModel, Field, EmailStr, conint, constr, computed_field
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    first_name : constr(min_length=3, max_length=50)  #constr → String ke liye constraints lagane ke liye use hota hai.
    Last_name : constr(min_length=3, max_length=50)
    email : EmailStr
    age : conint(gt=0)  #conint → Integer ke liye constraints lagane ke liye use hota hai. gt → greater than (age > 0)
    password : constr(min_length=8)

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.Last_name}"
    
    def age_group(self) -> str:
        if self.age < 18:
            return "Minor"
        elif 18 <= self.age < 65:
            return "Adult"
        else:
            return "Senior"
    
user_data = {
    "first_name": "Anant",
    "Last_name": "Awasthi",
    "email": "anantawasthi773@gmail.com",
    "age": 25,
    "password": "Anant@123"
}

user= User(**user_data)


print(user)
print(user.full_name)
print(user.age_group())