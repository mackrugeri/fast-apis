from fastapi import APIRouter

routes = APIRouter(
    prefix='/products',
    tags=['products']
)

@routes.get('/')
def get_product():
    return {"message": "Get product"}

@routes.post('/{product_id}')
def post_product(product_id: int):
    return {"message": "post product"}

@routes.put('/{product_id}')
def put_product(product_id: int):
    return {"message": "put products"}

@routes.patch('/{product_id}')
def patch_product(product_id: int):
    return {"message": "patch products"}

@routes.delete('/{product_id}')
def delete_product(product_id: int):
    return {"message": "delete products"}
