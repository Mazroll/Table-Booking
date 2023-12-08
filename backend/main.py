from fastapi import FastAPI
from api import customers
from contextlib import asynccontextmanager
from beanie.operators import In





from typing import Union

from database.mongoClient import initDB



@asynccontextmanager
async def lifespan(app:FastAPI):
    await initDB()
    yield

    
    
    
app=FastAPI(lifespan=lifespan)







@app.get('/')
async def main_page():
    return {'message':'Homepage will be here if logged in else will be redirected to login page'}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="info",reload=True)