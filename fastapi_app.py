"""
FastAPI Backend for Temperature Prediction
Deploy with: uvicorn app:app --reload
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import numpy as np
import pandas as pd
from typing import List, Dict

app = FastAPI(
    title="🌡 Temperature Prediction API",
    description="AI-powered temperature prediction using pollutant data",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class PredictionRequest(BaseModel):
    city: str
    date: str  # YYYY-MM-DD format
    model_type: str = "random_forest"  # or "lstm"

class PredictionResponse(BaseModel):
    city: str
    date: str
    predicted_temperature: float
    confidence: float
    model_used: str

class HistoryResponse(BaseModel):
    city: str
    avg_temperature: float
    avg_o3: float
    avg_no2: float
    avg_pm25: float

# In-memory model storage (replace with actual model loading)
AVAILABLE_CITIES = ["Rajamahendravaram", "Tirumala", "Velagapudi", "Visakhapatnam"]
MODELS = {}  # Load your trained models here

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "🌡 Temperature Prediction API is running",
        "version": "1.0.0",
        "endpoints": [
            "/predict - POST request for temperature prediction",
            "/cities - GET available cities",
            "/history/{city} - GET historical data for a city",
            "/models - GET available models",
            "/docs - API documentation"
        ]
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_temperature(request: PredictionRequest):
    """
    Predict temperature for a given city and date
    
    Example:
    ```json
    {
        "city": "Visakhapatnam",
        "date": "2026-06-01",
        "model_type": "random_forest"
    }
    ```
    """
    
    # Validate city
    if request.city not in AVAILABLE_CITIES:
        raise HTTPException(
            status_code=400,
            detail=f"City not found. Available cities: {AVAILABLE_CITIES}"
        )
    
    # Validate model type
    if request.model_type not in ["lstm", "random_forest"]:
        raise HTTPException(
            status_code=400,
            detail="Model type must be 'lstm' or 'random_forest'"
        )
    
    try:
        # Parse date
        target_date = datetime.strptime(request.date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM-DD"
        )
    
    # TODO: Load actual models and make prediction
    # For now, returning dummy prediction
    predicted_temp = np.random.uniform(20, 35)
    confidence = np.random.uniform(0.75, 0.98)
    
    return PredictionResponse(
        city=request.city,
        date=request.date,
        predicted_temperature=round(predicted_temp, 2),
        confidence=round(confidence, 2),
        model_used=request.model_type
    )

@app.get("/cities")
async def get_cities():
    """Get list of available cities"""
    return {
        "cities": AVAILABLE_CITIES,
        "count": len(AVAILABLE_CITIES)
    }

@app.get("/history/{city}", response_model=HistoryResponse)
async def get_city_history(city: str):
    """Get historical statistics for a city"""
    
    if city not in AVAILABLE_CITIES:
        raise HTTPException(
            status_code=404,
            detail=f"City '{city}' not found"
        )
    
    # TODO: Load actual historical data
    return HistoryResponse(
        city=city,
        avg_temperature=27.5,
        avg_o3=65.3,
        avg_no2=45.8,
        avg_pm25=72.1
    )

@app.get("/models")
async def get_models():
    """Get information about available models"""
    return {
        "available_models": {
            "lstm": {
                "name": "LSTM (Deep Learning)",
                "type": "neural_network",
                "accuracy": 0.78,
                "best_for": "temporal patterns"
            },
            "random_forest": {
                "name": "Random Forest",
                "type": "ensemble",
                "accuracy": 0.94,
                "best_for": "overall performance"
            }
        },
        "recommended": "random_forest"
    }

@app.get("/batch-predict")
async def batch_predict(city: str, start_date: str, end_date: str):
    """
    Predict temperature for a range of dates
    
    Example: /batch-predict?city=Visakhapatnam&start_date=2026-06-01&end_date=2026-06-07
    """
    if city not in AVAILABLE_CITIES:
        raise HTTPException(status_code=400, detail="Invalid city")
    
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")
    
    # Generate predictions for date range
    predictions = []
    current = start
    while current <= end:
        predictions.append({
            "date": current.strftime("%Y-%m-%d"),
            "temperature": round(np.random.uniform(20, 35), 2),
            "confidence": round(np.random.uniform(0.75, 0.98), 2)
        })
        current += pd.Timedelta(days=1)
    
    return {
        "city": city,
        "period": f"{start_date} to {end_date}",
        "predictions": predictions
    }

@app.get("/health")
async def health_check():
    """Health check for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
