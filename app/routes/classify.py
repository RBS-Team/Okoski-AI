from fastapi import APIRouter
from app.schemas.request import RequestText
from app.services.service import predict_text

router = APIRouter()

@router.post("/classify")
def classify(request: RequestText):
    return predict_text(request.text)


@router.get("/health")
def health():
    return {"status": "ok"}