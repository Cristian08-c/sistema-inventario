from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
import json


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "43200"))


# 🔍 Diagnóstico
print("SECRET_KEY:", bool(SECRET_KEY))
print("ALGORITHM:", ALGORITHM)
print("ACCESS_TOKEN_EXPIRE_MINUTES:", ACCESS_TOKEN_EXPIRE_MINUTES)

if ACCESS_TOKEN_EXPIRE_MINUTES is None:
    raise RuntimeError("⚠️ No se encontró ACCESS_TOKEN_EXPIRE_MINUTES en el .env")

ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def guardar_token(token):
    with open("session.json", "w") as f:
        json.dump({"access_token": token}, f)

def obtener_token():
    try:
        with open("session.json", "r") as f:
            return json.load(f).get("access_token")
    except FileNotFoundError:
        return None
def borrar_token():
    if os.path.exists("session.json"):
        os.remove("session.json")    



