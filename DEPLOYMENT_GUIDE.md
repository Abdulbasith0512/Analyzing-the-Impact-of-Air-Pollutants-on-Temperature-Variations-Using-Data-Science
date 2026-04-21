# 🚀 Deployment Guide - Temperature Prediction App

## Quick Start Options

### **Option 1: Streamlit (Easiest) ⭐**
Best for: Data scientists, quick demos, interactive dashboards

#### Local Setup:
```bash
pip install streamlit
streamlit run streamlit_app.py
```
Visit: `http://localhost:8501`

#### Deploy on Streamlit Cloud (Free):
1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Click "Deploy"

---

### **Option 2: FastAPI (Production-Ready)**
Best for: Building robust APIs, mobile apps, microservices

#### Local Setup:
```bash
pip install fastapi uvicorn
uvicorn fastapi_app:app --reload
```
Visit: `http://localhost:8000/docs` (Swagger UI)

#### Deploy on Heroku:
```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create temp-prediction-app

# Deploy
git push heroku main

# View
heroku open
```

#### Deploy on AWS:
- Use AWS EC2, Elastic Beanstalk, or Lambda
- Install dependencies in server
- Run: `nohup uvicorn fastapi_app:app &`

---

### **Option 3: Docker Container**
Best for: Consistency across environments, cloud deployment

#### Build & Run Locally:
```bash
# Build image
docker build -t temp-prediction:latest .

# Run Streamlit
docker run -p 8501:8501 temp-prediction:latest

# OR Run FastAPI
docker run -p 8000:8000 temp-prediction:latest \
  sh -c "uvicorn fastapi_app:app --host 0.0.0.0"
```

#### Deploy to Cloud (Docker):
- **AWS ECR + ECS**: Upload to Elastic Container Registry
- **Google Cloud Run**: `gcloud run deploy`
- **Azure Container Instances**: `az container create`
- **DigitalOcean**: Use their App Platform

---

### **Option 4: Hugging Face Spaces (Free) 🤗**
Best for: Free hosting, no credit card needed

1. Create account on huggingface.co
2. Create new Space (choose Streamlit)
3. Upload `streamlit_app.py`
4. Push to GitHub and link
5. Auto-deployed!

---

### **Option 5: Traditional Web App (Flask/Django)**

#### Flask Example:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Your prediction logic here
    return jsonify({"temperature": 28.5})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## Recommended Path

### For Quick Demo:
1. **Streamlit** → Deploy on Streamlit Cloud (Free, 1 click)

### For Production API:
1. **FastAPI** → Deploy on Heroku or AWS
2. Add authentication (API keys)
3. Set up monitoring & logging

### For Enterprise:
1. **Docker** → Kubernetes deployment
2. Add load balancing
3. Implement CI/CD pipeline

---

## Model Deployment Tips

### Save Models (Add to your notebook):
```python
import pickle

# Save LSTM models
for city in models:
    pickle.dump(models[city], open(f'models/lstm_{city}.pkl', 'wb'))

# Save Random Forest models
for city in rf_models:
    pickle.dump(rf_models[city], open(f'models/rf_{city}.pkl', 'wb'))

# Save scalers
for city in scalers:
    pickle.dump(scalers[city], open(f'models/scaler_{city}.pkl', 'wb'))
```

### Load Models in Deployment:
```python
import pickle

models = {}
for city in ['Rajamahendravaram', 'Tirumala', 'Velagapudi', 'Visakhapatnam']:
    models[city] = pickle.load(open(f'models/lstm_{city}.pkl', 'rb'))
```

---

## Environment Variables (.env)
```
MODEL_TYPE=random_forest
DATA_PATH=./final_merged_dataset.csv
DEBUG=False
```

---

## Cost Estimates

| Platform | Cost | Best For |
|----------|------|----------|
| Streamlit Cloud | Free | Demos, dashboards |
| Heroku | $50/month | Small APIs |
| AWS (EC2) | $5-20/month | Production APIs |
| Hugging Face | Free | ML demos |
| Docker + K8s | Variable | Enterprise |

---

## Monitoring & Logging

Add to your deployment:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

---

## Next Steps

1. ✅ Choose deployment platform
2. ✅ Export models to .pkl or .h5 files
3. ✅ Update app.py with model loading
4. ✅ Test locally
5. ✅ Deploy!

---

## Questions?
Check official docs:
- Streamlit: https://docs.streamlit.io
- FastAPI: https://fastapi.tiangolo.com
- Docker: https://docs.docker.com
