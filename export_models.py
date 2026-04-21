"""
Model Export Script
Run this after training models in your notebook to save them for deployment

Usage:
    python export_models.py
"""

import pickle
import os
import json
from datetime import datetime

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

def export_models(models, rf_models, scalers, city_data):
    """
    Export trained models to disk
    
    Parameters:
    - models: dict of trained LSTM models
    - rf_models: dict of trained Random Forest models
    - scalers: dict of MinMaxScalers
    - city_data: dict of processed city data
    """
    
    export_count = 0
    
    # Export LSTM models
    print("📦 Exporting LSTM models...")
    for city, model in models.items():
        try:
            model.save(f'models/lstm_{city}.h5')
            print(f"✅ LSTM {city}: models/lstm_{city}.h5")
            export_count += 1
        except Exception as e:
            print(f"❌ Error exporting LSTM {city}: {e}")
    
    # Export Random Forest models
    print("\n📦 Exporting Random Forest models...")
    for city, model in rf_models.items():
        try:
            with open(f'models/rf_{city}.pkl', 'wb') as f:
                pickle.dump(model, f)
            print(f"✅ RF {city}: models/rf_{city}.pkl")
            export_count += 1
        except Exception as e:
            print(f"❌ Error exporting RF {city}: {e}")
    
    # Export Scalers
    print("\n📦 Exporting Scalers...")
    for city, scaler in scalers.items():
        try:
            with open(f'models/scaler_{city}.pkl', 'wb') as f:
                pickle.dump(scaler, f)
            print(f"✅ Scaler {city}: models/scaler_{city}.pkl")
            export_count += 1
        except Exception as e:
            print(f"❌ Error exporting scaler {city}: {e}")
    
    # Export metadata
    print("\n📦 Exporting metadata...")
    metadata = {
        "export_date": datetime.now().isoformat(),
        "models_exported": {
            "lstm_count": len(models),
            "rf_count": len(rf_models),
            "scalers_count": len(scalers)
        },
        "cities": list(models.keys()),
        "model_types": ["LSTM", "Random Forest"],
        "features": list(city_data[list(city_data.keys())[0]].columns) if city_data else []
    }
    
    with open('models/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"✅ Metadata: models/metadata.json")
    
    print(f"\n{'='*50}")
    print(f"✅ Export Complete!")
    print(f"📊 Total artifacts exported: {export_count + 1}")
    print(f"📁 Location: ./models/")
    print(f"{'='*50}")
    
    return True


def load_models_for_deployment():
    """
    Load models for use in deployment
    
    Returns:
    - models: dict of LSTM models
    - rf_models: dict of Random Forest models
    - scalers: dict of scalers
    - metadata: deployment metadata
    """
    
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    
    models = {}
    rf_models = {}
    scalers = {}
    
    # Load metadata
    with open('models/metadata.json', 'r') as f:
        metadata = json.load(f)
    
    cities = metadata['cities']
    
    print("🔄 Loading models...")
    
    # Load LSTM models
    for city in cities:
        try:
            model = load_model(f'models/lstm_{city}.h5')
            models[city] = model
            print(f"✅ Loaded LSTM: {city}")
        except Exception as e:
            print(f"❌ Error loading LSTM {city}: {e}")
    
    # Load Random Forest models
    for city in cities:
        try:
            with open(f'models/rf_{city}.pkl', 'rb') as f:
                model = pickle.load(f)
            rf_models[city] = model
            print(f"✅ Loaded RF: {city}")
        except Exception as e:
            print(f"❌ Error loading RF {city}: {e}")
    
    # Load Scalers
    for city in cities:
        try:
            with open(f'models/scaler_{city}.pkl', 'rb') as f:
                scaler = pickle.load(f)
            scalers[city] = scaler
            print(f"✅ Loaded Scaler: {city}")
        except Exception as e:
            print(f"❌ Error loading scaler {city}: {e}")
    
    print(f"\n✅ All models loaded successfully!")
    
    return models, rf_models, scalers, metadata


if __name__ == "__main__":
    print("🚀 Model Export Tool")
    print("="*50)
    print("\nUsage:")
    print("1. Export models from your notebook:")
    print("   export_models(models, rf_models, scalers, city_data)")
    print("\n2. In your deployment app, load models:")
    print("   models, rf_models, scalers, metadata = load_models_for_deployment()")
    print("="*50)
