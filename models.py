from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


products = [{
  "id": 0,
  "name": "string",
  "category": "string",
  "price": 0,
  "stock": 10
  
},
{
  "id": 1,
  "name": "string",
  "category": "string",
  "price": 0,
  "stock": 10
  
}        
]

categories = [{
    "id": 0,
    "name": "Comestibles"
},
{
    "id": 1,
    "name": "Aseo"    
}              
              ]

class Category(BaseModel):
    Id: int
    
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
