from fastapi import FastAPI
import json


app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/patients")
def get_patients():
    data = load_data()
    return data

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}


#Path Parameters
@app.get("/patients/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()

    for patient in data:
        if patient["patient_id"] == patient_id:
            return patient

    return {"message": "Patient not found."}
