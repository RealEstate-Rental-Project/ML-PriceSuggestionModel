from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(title="Property Multi-Model Prediction Service")

# 1. Chargement des deux modèles et de leurs préprocesseurs
# Modèle Mensuel
model_monthly = joblib.load('monthly/property_price_model.joblib')
prep_monthly = joblib.load('monthly/preprocessor.joblib')

# Modèle Daily
model_daily = joblib.load('daily/model_daily.joblib')
prep_daily = joblib.load('daily/preprocessor_daily.joblib')

# 2. Schémas de données (Pydantic)
class Input(BaseModel):
    city: str
    country: str
    longitude: float
    latitude: float
    sqm: int
    total_rooms: int
    nombre_etoiles: int



# --- ROUTES ---

@app.post("/predict/monthly")
def predict_monthly(data: Input):
    df = pd.DataFrame([data.dict()])
    processed = prep_monthly.transform(df)
    price_wei = model_monthly.predict(processed)[0]
    return {
        "type": "MONTHLY",
        "price_wei": int(price_wei),
        "price_eth": round(price_wei / 10**18, 4)
    }

@app.post("/predict/daily")
def predict_daily(data: Input):
    df = pd.DataFrame([data.dict()])
    processed = prep_daily.transform(df)
    price_wei = model_daily.predict(processed)[0]
    return {
        "type": "DAILY",
        "price_wei": int(price_wei),
        "price_eth": round(price_wei / 10**18, 4)
    }


if __name__ == "__main__":
    import uvicorn
    # Le port 8000 correspond à celui exposé dans votre Dockerfile
    uvicorn.run(app, host="0.0.0.0", port=8000)
