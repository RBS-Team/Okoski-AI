from app.model.classifier import model_pipeline

def predict_text(text: str):

    user_text = text.lower().strip()

    prediction = model_pipeline.predict([user_text])[0]

    try:
        decision_values = model_pipeline.decision_function([user_text])
        confidence = float(decision_values.max())
    except:
        confidence = 0.0

    return {
        "query": text,
        "recommended_service": prediction,
        "confidence_score": round(confidence, 2)
    }