from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Product(BaseModel):
    id: int
    
    name: str
    
    category: str
    
    price: float
    

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
           
    
