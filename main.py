from fastapi import FastAPI 
from database import engine
from models import Base
from router import tasks
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(tasks.router)

