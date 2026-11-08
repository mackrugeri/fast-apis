from fastapi import APIRouter

routes= APIRouter(
    prefix="/payments",
    tags=['payment']
)

@routes.get('/')
def get_payments():
    return {"message": "Get payments"}

@routes.post('/{payments_id}')
def post_payments(payments_id: int):
    return {"message": "post payments"}

@routes.put('/{payments_id}')
def put_payments(payments_id: int):
    return {"message": "put paymentss"}

@routes.patch('/{payments_id}')
def patch_payments(payments_id: int):
    return {"message": "patch paymentss"}

@routes.delete('/{payments_id}')
def delete_payments(payments_id: int):
    return {"message": "delete paymentss"}
