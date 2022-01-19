from fastapi import FastAPI

from models import user_model
from routers import user
from utilities.database import engine

app = FastAPI()

user_model.Base.metadata.create_all(engine)

app.include_router(user.router)
