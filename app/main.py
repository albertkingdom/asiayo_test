from fastapi import FastAPI, HTTPException
from app.handlers.order_handler import OrderHandler
from app.models.order import Order
from app.services.transformers import OrderTransformer
from app.services.validators import OrderValidator

app = FastAPI()

@app.post("/api/orders")
async def create_order(order: Order):
    validator = OrderValidator()
    transformer = OrderTransformer()
    handler = OrderHandler(validator=validator, transformer=transformer)
    result = handler.process_order(order.dict())
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
