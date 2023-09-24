from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

tutors = [{"name": "andrew", "id" : 1},{"name": "kareena", "id": 2},{"name": "lizzie", "id": 3}, {"name": "emma", "id": 4}]

class Tutor(BaseModel):
    name: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/tutors")
async def get_tutors():
    return tutors

@app.post("/addTutor/{id}")
async def add_tutor(tutor: Tutor, id: int):
    tutors.append({"name": tutor.name, "id": id})
    return {"added": tutor, "withid": id}