from fastapi import FastAPI
from models import Product,products
from auth import Router as auth_router
import requests
import json
from fastapi import Depends, HTTPException
import utils.jwt_handler_util
from fastapi.security import OAuth2PasswordBearer
import main

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = utils.jwt_handler_util.verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return payload



app = FastAPI()

app.include_router(auth_router)

app.get("/")
def read_products():
    return {"Hello":"World"}


@app.get("/products")
def read_products():
    return products


@app.get("/products/{product_id}")
def read_product_by_id(product_id : int):
   for producto in products:
       if producto["id"] == product_id:
           return{"producto":producto}
   return {"message":"Producto no encotrado"}


@app.post("/products")
def create_products(product: Product):
    products.append(product)
    return{"message:":"Producto creado correctamente","producto": product}


@app.put("/products/{product_id}")
def update_product(
   product_id:int,
    
    name: str,
    
    category: str,
    
    price: float
):
    for product in products:
       if product["id"] == product_id:
           
           product["name"]= name
           
           product["category"]= category
           
           product["price"]= price
           
    
    return {"Se actualizo el producto correctamente": products}


@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
    
    return products





class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("Iniciando login para:", self.username)
        url = "http://127.0.0.1:8000/auth/login/"
        payload = {
            "Username": self.username,
            "Password": self.password
        }

        try:
            response = requests.post(url, json=payload)
            print("📡 Status:", response.status_code)
            print("📦 Respuesta:", response.text)
        except Exception as e:
            print("⚠️ Error al hacer la request:", e)
            return None

        try:
            data = response.json()
        except Exception:
            print("⚠️ Error interpretando respuesta:", response.text)
            return None

        if response.status_code == 200 and data.get("status") == "ok":
            token = data.get("access_token")
            if token:
                print("✅ Login exitoso. Token recibido.")
                return token
                
        else:
            print(f"❌ Error en login: {data.get('detail', 'Error desconocido')}")
            return None

    def signup(self):
        print("Iniciando registro para:", self.username)
        url = "https://api-test-0cxg.onrender.com/auth/register/"
        payload = {
            "Username": self.username,
            "Password": self.password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Usuario registrado con éxito")
        elif response.status_code == 400:
            print("Error en el registro")


        


