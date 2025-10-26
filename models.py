from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


products = [{
  "id": 0,
  "name": "string",
  "category": "string",
  "price": 0,
  
},
{
  "id": 1,
  "name": "string",
  "category": "string",
  "price": 0,
  
}        
]




class Product(BaseModel):

    Id: int

    name: str
    
    category: str
    
    price: float
    


class Login(BaseModel):
    Username: str
    Password: str

class Register(BaseModel):
    Username: str
    Password: str
