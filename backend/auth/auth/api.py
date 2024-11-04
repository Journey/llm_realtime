from fastapi import Depends, APIRouter
from enum import Enum
from pydantic import BaseModel
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

from backend.auth.auth.auth import generate_token
from backend.auth.auth.token import Token
from backend.auth.auth.user import User

class TokenType(str, Enum):
    refresh_token = "refresh"
    id_token = "id"
    bear_token = "bear"


auth_router = APIRouter()

@auth_router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    

@auth_router.post("/login", include_in_schema=True)
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    login with usr/pwd and return Token if everything is ok.
    """
    username = form.username
    password = form.password
    print(username)
    # todo:: verify username / password

    token = generate_token()
    return {"access_token": token, "token_type": "bear"}

@auth_router.get("/status")
async def status():
    return "it works!!!"
