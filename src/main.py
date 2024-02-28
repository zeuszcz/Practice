from fastapi import FastAPI


from src.routers.cart import router as router_cart
from src.routers.product_component import router as router_component
from src.routers.product import router as router_product
from src.routers.cart_item import router as router_cart_item
from src.routers.service import router as router_service
from src.routers.product_type import router as router_product_type
from src.routers.build import router as router_build
from dotenv import load_dotenv


app = FastAPI(
    title="calculator"
)



app.include_router(router_cart)
app.include_router(router_component)
app.include_router(router_product)
app.include_router(router_cart_item)
app.include_router(router_service)
app.include_router(router_product_type)
app.include_router(router_build)
