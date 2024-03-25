from fastapi import FastAPI
from app.routes import router as router_home
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(router_home)
app.mount("/static", StaticFiles(directory="static"), name="static")
