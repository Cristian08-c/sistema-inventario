from fastapi import FastAPI,APIRouter
from models import Login, Register

Router = APIRouter(prefix="/auth",tags=["Auth"])

@Router.post("/login/")
def Login(credentials: Login):
    user = credentials.Username
    password = credentials.Password
    return{"User:":user, "Password": password}


