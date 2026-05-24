import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model.pkl"

model_pipeline = joblib.load(MODEL_PATH)