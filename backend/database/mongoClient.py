from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import WriteRules, init_beanie
from models.customers import CustomerLogin, CustomerSignUp





import os


DEBUG = config('DEBUG', default=False, cast=bool)
MONGODB_URI=config('MONGODB_URI')







async def initDB():
    client = AsyncIOMotorClient(MONGODB_URI)
    await init_beanie(database=client["TabelManagementSystem"],document_models=[CustomerLogin,CustomerSignUp])

# def get_mongodb_client() -> MongoClient:
#     return MongoClient(MONGODB_URI)

                        