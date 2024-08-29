from pydantic import BaseModel


class Product(BaseModel):
    title: str
    category_id: str
    price: float
    currency_id: str = "BRL"
    available_quantity: int
    buying_mode: str = "buy_it_now"
    condition: str = "new"
    listing_type_id: str = "bronze"