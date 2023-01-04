from fastapi import FastAPI
import model
from config import engine
from router import router


model.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router,prefix="/payment",tags=["payment"])