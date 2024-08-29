from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def list_products():
    return [{"product_id": "123", "name": "Product 1"}, {"product_id": "456", "name": "Product 2"}]

@router.get("/{product_id}")
def get_product(product_id: str):
    if product_id == "123":
        return {"product_id": "123", "name": "Product 1"}
    raise HTTPException(status_code=404, detail="Product not found")