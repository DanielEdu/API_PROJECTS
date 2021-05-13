"""
http://localhost:8000/docs
"""
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import spacy


app = FastAPI()
nlp_en = spacy.load("es_core_news_sm")

class Article(BaseModel):
    content: str
    comment: List[str] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/article/")
async def recognize_entities(article: Article, big_model: bool = False):
    doc_en = nlp_en(article.content)
    ents = []
    for ent in doc_en.ents:
        ents.append({"text": ent.text, "label_": ent.label_})
    return {
        "message": article.content,
        "ents": ents,
        "big_model": big_model
        }
