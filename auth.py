from fastapi import FastAPI,APIRouter, HTTPException
from models import Login, Register
from utils.auth_util import hash_password,verifypassword
from db import *

Router = APIRouter(prefix="/auth",tags=["Auth"])



@Router.post("/login/")
def Login(credentials: Login):

    user = credentials.Username
    password = credentials.Password


    DataUser = read_user_by_username(user)

    if DataUser is None:
         raise HTTPException(status_code=404,detail="User not found")

    if DataUser["username"]:
      
        if not verifypassword(password,DataUser["password"]):
            raise HTTPException(status_code=400,detail="Credenciales incorrectas")
        else:
            return {"status": "ok", "message": "Login exitoso"}
    else:
        raise HTTPException(status_code=404,detail="contraseña incorrecta")




@Router.post("/register/")
def Register(credentials: Register):
    
    user = credentials.Username
    password = credentials.Password

    HashedData = hash_password(password)

    create_user(user,HashedData,"none")

    raise HTTPException(status_code=200,detail="Registro exitoso")



