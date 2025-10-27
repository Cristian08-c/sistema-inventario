from fastapi import FastAPI
from models import Product,products, Category, categories
from auth import Router as auth_router

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


@app.get("/categories")
def read_categories():
    return categories


@app.post("/products")
def create_products(product: Product):
    products.append(product)
    return{"message:":"Producto creado correctamente","producto": product}


@app.post("/categories")
def create_categories(category:Category):
    categories.append(category)
    return{"message":"Categoria creada correctamente","Categoria":category}


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


@app.put("/categories/{category_id}")
def update_category(
   category_id:int,
    
    name: str,
):
    
    for category in categories:
       if category["id"] == category_id:
           
           category["name"]= name
           
          
    return {"Se actualizo el producto correctamente": categories}


@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
    
    return products


@app.delete("/categories/{category_id}")
def delete_category(category_id:int):
    for category in categories:
        if category["id"] == category_id:
            categories.remove(category)
    
    return categories

