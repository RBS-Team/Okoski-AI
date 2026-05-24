from fastapi import FastAPI
from app.routes.classify import router

app = FastAPI(title="AI Okoski")

app.include_router(router)