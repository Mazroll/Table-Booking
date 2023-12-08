from datetime import timedelta
import json
from models.customers import CustomerLogin, CustomerSignUp,CustomerLoginRead
from main import app
from decouple import config
from dependencies.createJWT import create_jwt_token
from beanie import WriteRules
from fastapi.security import OAuth2PasswordBearer


@app.post('/create-user',response_model=CustomerLoginRead)
async def createUser(userInfo:CustomerSignUp):
    user_data_dict = userInfo.model_dump()
    jwtToken=create_jwt_token(userInfo.model_dump(mode='python'),timedelta(minutes=int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))))
    user_data_dict['token']=jwtToken
    user_data_dict['token']=jwtToken
    signUpData=CustomerLogin(**user_data_dict)
    await signUpData.insert(link_rule=WriteRules.WRITE)
    return CustomerLoginRead(**signUpData.model_dump(),token=jwtToken)


@app.post('/login')
async def createUser(userInfo:CustomerLogin):
    ## need to generate jwt authentication first
    return {'message':"User LoggedIn Successfully","data":userInfo.model_dump()} 