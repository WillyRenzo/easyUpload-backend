from fastapi import FastAPI
from main.api.routers import products

app = FastAPI()

# Inclui as rotas dos módulos
app.include_router(products.router, prefix="/products", tags=["Products"])
   
@app.get("/") 
async def health():     
  return { "status": 204, "message": "Server is running!"}