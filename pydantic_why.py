from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, conint, constr
from typing import Optional, List, Dict

app = FastAPI()

# class Patient(BaseModel):
#     name : str
#     age: int
#     email : str
#     Phone_No : int

# patient = Patient(name="Anant_Awasthi", age=25, email="anant@example.com", Phone_No=1234567890)

# print(patient)


#1.) Type Validation


# class Patient(BaseModel):
#     name : str
#     age: int
#     email: str
#     contact_details: Dict[str, str]
#     married_status: bool
#     allergies: Optional[List[str]] = None
#     weight: float

# patient = Patient(
#     name="Anant_Awasthi",
#     age="25",
#     email="anant@example.com",
#     contact_details={
#         "phone": "1234567890",
#         "address": "New Delhi, India"},
#     married_status=False,
#     allergies=["peanuts","Dust","pollen"],
#     weight=70.5
# )

# print (patient)


#2.) Data Validation (Field Validation)

class Patient2(BaseModel):
    name : str = Field(..., min_length=3, max_length=50, description="Name must be between 3 and 50 characters")
    age: int = Field(gt=0, description="Age must be a positive integer")
    email: EmailStr
    contact_details: Dict[str, str] = Field(..., description="Contact details must be a dictionary with phone and address")
    married_status: bool
    allergies: Optional[List[str]] = None 
    weight: float = Field (..., gt=0, description="Weight must be a positive float")

patient2 = Patient2(
    name="Anant_Awasthi",
    age=25,
    email="anant@example.com",
    contact_details={
        "phone": "1234567890",
        "address": "New Delhi, India"
    },
    married_status=False,
    allergies=["peanuts", "Dust", "pollen"],
    weight=70.5
)

print(patient2)


