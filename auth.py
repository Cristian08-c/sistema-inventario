from fastapi import FastAPI,APIRouter, HTTPException
from models import Login, Register
from utils.auth_util import hash_password,verifypassword
from db import *

Router = APIRouter(prefix="/auth",tags=["Auth"])



@Router.post("/login/")
def Login(credentials: Login):
    user = credentials.Username
    password = credentials.Password


    User,HashedPassword = read_user_by_username(user)

    if User:
        if not verifypassword(password,HashedPassword):
            raise HTTPException(status_code=400,detail="Credenciales incorrectas")
        else:
            raise HTTPException(status_code=200,detail="Login exitoso")


@Router.post("/register/")
def Login(credentials: Register):
    
    user = credentials.Username
    password = credentials.Password

    HashedData = hash_password(password)

    create_user(user,HashedData,"none")

    raise HTTPException(status_code=200,detail="Registro exitoso")



