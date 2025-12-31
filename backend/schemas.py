from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str


class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str


class RecommendationResponse(BaseModel):
    message: str
    recommendations: List[Product]