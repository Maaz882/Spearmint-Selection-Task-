from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from config import OPENAI_API_KEY
import json

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)

def recommend_products(user_query: str, products: list):
    prompt = PromptTemplate.from_template("""
You are an AI product recommendation assistant.

User request:
"{query}"

Available products:
{products}

Instructions:
- Recommend products ONLY from the given list.
- If no product matches the user request, return an empty list.
- Always return valid JSON in this format:

{{
  "message": string,
  "recommendations": [
    {{
      "id": number,
      "name": string,
      "price": number,
      "category": string
    }}
  ]
}}

Rules:
- If recommendations list is empty, message should say:
  "Sorry, no products match your request."
- If not empty, message should say:
  "Here are some products you may like."
- Do not include any explanation text outside JSON.
""")

    chain = prompt | llm

    response = chain.invoke({
        "query": user_query,
        "products": products
    })

    try:
        return json.loads(response.content)
    except:
        return {
            "message": "Sorry, something went wrong.",
            "recommendations": []
        }