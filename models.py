from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


wallet = 0.0


historial_compras = []


products = [{
  "id": 1,
  "name": "Pan",
  "category": "Comestibles",
  "price": 2,
  "stock": 200
  
},
{
  "id": 2,
  "name": "Lechuga",
  "category": "Vegetales",
  "price": 3,
  "stock": 200
}        
]

categories = [{
    
    "name": "Comestibles"
},
{
    
    "name": "Aseo"    
}              
              ]

class Category(BaseModel):
    
    name: str



class Product(BaseModel):

    Id: int

    name: str
    
    category: str
    
    price: float
    
    stock: int
    


class Login(BaseModel):
    Username: str
    Password: str

class Register(BaseModel):
    Username: str
    Password: str
