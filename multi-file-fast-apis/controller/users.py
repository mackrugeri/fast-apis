from fastapi import APIRouter

routes = APIRouter(
    prefix="/users",
    tags = ['user']
)

@routes.get('/')
def get_users():
    return {"message": "Get users"}

@routes.post('/{user_id}')
def post_users(user_id: int):
    return {"message": "Post users"}

@routes.put('/{user_id}')
def put_users(user_id: int):
    return {"message": "Put users"}

@routes.patch('/{user_id}')
def patch_users(user_id: int):
    return {"message": "Patch users"}

@routes.delete('/{user_id}')
def delete_users(user_id: int):
    return {"message": "Delete users"}