from fastapi import FastAPI,APIRouter, HTTPException
from models import Login, Register
from utils.auth_util import hash_password,verifypassword

Router = APIRouter(prefix="/auth",tags=["Auth"])

userdb =  "$2b$12$.sxw3jhvE3RWiwsspEnSWuYYfoyljE8JSQu1VKJyKwxRgRUhrDwHa"

@Router.post("/login/")
def Login(credentials: Login):
    user = credentials.Username
    password = credentials.Password



    if verifypassword(password,userdb):
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
    
    raise HTTPException(status_code=200,detail="Login exitoso")


@Router.post("/register/")
def Login(credentials: Register):
    
    user = credentials.Username
    password = credentials.Password

    HashedData = hash_password(password)

    raise HTTPException(status_code=200,detail="Registro exitoso")



