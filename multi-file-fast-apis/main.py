from fastapi import FastAPI
from controller import users, products, payments, orders

app = FastAPI(title="My Api")

app.include_router(users.routes)
app.include_router(products.routes)
app.include_router(payments.routes)
app.include_router(orders.routes)

