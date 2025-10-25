from fastapi import FastAPI
from router import Product, products

app = FastAPI()



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


