from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="1Fi Marketplace Mock API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EMIPlan(BaseModel):
    id: str
    duration_months: int
    interest_rate: float
    monthly_installment: float
    total_cost: float

class ProductVariant(BaseModel):
    id: str
    name: str
    color_hex: str
    image_url: str
    in_stock: bool

class Product(BaseModel):
    id: str
    name: str
    brand: str
    price: float
    image_url: str
    description: str
    variants: List[ProductVariant]
    emi_plans: List[EMIPlan]

MOCK_PRODUCTS = [
    Product(
        id="prod_1",
        name="MacBook Air M3",
        brand="Apple",
        price=114900.00,
        image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&q=80",
        description="Supercharged by M3. The ultimate thin and light laptop.",
        variants=[
            ProductVariant(
                id="v1",
                name="Midnight",
                color_hex="#2E3642",
                image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&q=80",
                in_stock=True
            ),
            ProductVariant(
                id="v2",
                name="Starlight",
                color_hex="#F0E4D3",
                image_url="https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=800&q=80",
                in_stock=True
            )
        ],
        emi_plans=[
            EMIPlan(id="emi_1_6", duration_months=6, interest_rate=0.0, monthly_installment=19150.00, total_cost=114900.00),
            EMIPlan(id="emi_1_12", duration_months=12, interest_rate=0.0, monthly_installment=9575.00, total_cost=114900.00)
        ]
    ),
    Product(
        id="prod_2",
        name="Samsung Galaxy S24 Ultra",
        brand="Samsung",
        price=129999.00,
        image_url="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=800&q=80",
        description="Galaxy AI is here. Welcome to the era of mobile AI.",
        variants=[
            ProductVariant(
                id="v3",
                name="Titanium Black",
                color_hex="#000000",
                image_url="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=800&q=80",
                in_stock=True
            )
        ],
        emi_plans=[
            EMIPlan(id="emi_2_9", duration_months=9, interest_rate=0.0, monthly_installment=14444.33, total_cost=129999.00)
        ]
    )
]

@app.get("/api/products", response_model=List[Product])
async def get_products():
    return MOCK_PRODUCTS

@app.get("/api/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = next((p for p in MOCK_PRODUCTS if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product