import httpx
import time
import requests
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/')
def home():
    return {"message": "hello world"}

@app.get('/employee/{employee_id}')
def get_employee(employee_id: int):
    return {"id": employee_id }


@app.get('/sync')
def sync_endpoint():
    time.sleep(5)
    return {"message": "Sync completed"}


@app.get('/async')
async def async_endpoint():
    await time.sleep(5)
    return {"message": "Async completed"}

@app.post('/create')
def create_user():
    return {'message': 'user created'}


@app.put('/update/{user_id}')
def update_user(user_id: int):
    return {'message': 'user update {user_id}'}


@app.patch('/patch/{user_id}')
def patch_user(user_id: int):
    return {'message': 'user patch {user_id}'}


@app.delete('/delete/{user_id}')
def delete_user(user_id: int):
    return {'message': 'user delete {user_id}'}


class User(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: str


@app.post("/user", status_code=201)
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }
@app.get("/users")
def get_users(name: str,age: int,city: str):
    return {
        "name": name,
        "age": age,
        "city": city
    }


@app.get("/get_request_test")
def get_request():
    request = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    print(request.status_code)
    return request.json()



@app.get("/post_request_test")
def post_request():
    payload = {
        "name": "John",
        "email": "john@example.com"
    }

    request = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload,
        timeout=10

    )

    print(request.status_code)
    return request.json()


@app.put('/put_request_test/{id}')
def put_request(id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    print(url)
    request = requests.put(
        url,
        json={"title": "Updated", "body": "New content", "userId": id},
        timeout=10
    )

    return request.json


@app.patch('/patch_request_test/{id}')
def patch_request(id: int):
    url = "https://jsonplaceholder.typicode.com/posts{1}"

    request = requests.patch(
        url,
        json={"title": "New title"},
        timeout=10
    )

    return request.json


@app.get('/test-http-request')
async def test_http_request():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://jsonplaceholder.typicode.com/users/1",
            timeout=10
        )
    response.raise_for_status()
    return response.json()