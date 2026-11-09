from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: str

users = [
    {"id": 1, "name": "Ahsan"},
    {"id": 2, "name": "Ali"}
]

@app.get('/test-exception-handling/{user_id}')
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return ""

        raise HTTPException(
            status_code= 404,
            detail="User not found"
        )


@app.post('/user')
def post_user(user:User):
    return user