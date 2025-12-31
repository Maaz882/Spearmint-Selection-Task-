from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import QueryRequest, RecommendationResponse
from products import PRODUCTS
from ai_service import recommend_products

app = FastAPI(title="AI Product Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend", response_model=RecommendationResponse)
def recommend(data: QueryRequest):
    return recommend_products(data.query, PRODUCTS)