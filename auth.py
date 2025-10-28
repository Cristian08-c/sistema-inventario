from fastapi import APIRouter, HTTPException
from models import Login, Register
from utils.auth_util import hash_password, verifypassword
from utils.jwt_handler_util import create_access_token
from db import *

Router = APIRouter(prefix="/auth", tags=["Auth"])

# LOGIN
@Router.post("/login/")
def login(credentials: Login):
    print("Iniciando proceso de login para:", credentials.Username)
    username = credentials.Username
    password = credentials.Password

    DataUser = read_user_by_username(username)
    if DataUser is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not verifypassword(password, DataUser["password"]):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")


    try:
        access_token = create_access_token({"sub": username})
        print("🔑 Token creado:", access_token)
    except Exception as e:
        print("⚠️ Error creando token:", e)
        raise HTTPException(status_code=500, detail=f"Error al generar token: {e}")

    print("✅ Token generado:", access_token)

    return {
        "status": "ok",
        "message": "Login exitoso",
        "access_token": access_token,
        "token_type": "bearer"
    }

# REGISTER
@Router.post("/register/")
def register(credentials: Register):
    username = credentials.Username
    password = credentials.Password

    # Verificar si ya existe
    existing_user = read_user_by_username(username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")

    # Hashear y guardar
    hashed_password = hash_password(password)
    create_user(username, hashed_password, "none")

    return {"status": "ok", "message": "Registro exitoso"}



