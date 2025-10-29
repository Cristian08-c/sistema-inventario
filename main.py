from fastapi import FastAPI
from models import Product,products, Category, categories, wallet, historial_compras
from auth import Router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
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


@app.get("/Stock/{product_id}")
def read_stock(product_id: int):
    for producto in products:
        if producto["id"] == product_id:
            return{"El stock disponible es:":producto["stock"]}


@app.get("/categories")
def read_categories():
    return categories


@app.get("/Wallet")
def read_wallet():
    return wallet


@app.get("/compras")
def read_compras():
    return historial_compras


@app.post("/products")
def create_products(product: Product):
    for producto in products:
        if producto["id"] == product.Id:
            return {"Error":"Ya existe un producto con ese ID"}
    if product.price <= 0:
        return{"Error":"El precio debe ser mayor a 0"}
    if product.stock <= 0:
        return {"Error":"El stock no puede ser negativo"}
    
    new_product = {
        "id": product.Id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "stock": product.stock
    }
    
    products.append(new_product)
    return {"Message":"Producto publicado correctamente", "producto": new_product}
    


@app.post("/categories")
def create_categories(category:Category):
    for categoria in categories:
        if categoria["id"] == category.Id:
            return {"Error":"Ya existe una categoria con ese ID"}
        
    nueva_categoria = {
        "id": category.Id,
        "name": category.name
    }
        
    categories.append(nueva_categoria)
    return{"message":"Categoria creada correctamente","Categoria": nueva_categoria}


@app.post("/buy/{product_id}")
def buy_product(product_id:int, cantidad: int):
    global wallet
    for producto in products:
        if producto["id"] == product_id:
            if producto["stock"] < cantidad:
                return {"Error":"No hay suficiente Stock disponible"}
        
            total_price = producto["price"] * cantidad
            producto["stock"] -= cantidad
            wallet += total_price
            
            
            compra = {
                "product_id": product_id,
                "product name":producto["name"],
                "cantidad": cantidad,
                "total pagado":total_price,
                "stock restante":producto["stock"]
            }
            historial_compras.append(compra)
            
            return {
            "message": "Compra realizada correctamente",
            "total pagado":total_price,
            "nuevo stock":producto["stock"],
            "cartera actual": wallet
        }
    return{"Error":"Producto no encontrado"}
            
       
            
            
        
        
      
       
    


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
       return{"Error":" Categoria no encontrada"}


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

