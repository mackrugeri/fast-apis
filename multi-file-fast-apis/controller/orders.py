from fastapi import APIRouter

routes = APIRouter(
    prefix='/orders',
    tags=["orders"]
)

@routes.get('/')
def get_order():
    return {"message": "Get order"}

@routes.post('/{order_id}')
def post_order(order_id: int):
    return {"message": "post order"}

@routes.put('/{order_id}')
def put_order(order_id: int):
    return {"message": "put orders"}

@routes.patch('/{order_id}')
def patch_order(order_id: int):
    return {"message": "patch orders"}

@routes.delete('/{order_id}')
def delete_order(order_id: int):
    return {"message": "delete orders"}
