FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# For Streamlit
EXPOSE 8501

# For FastAPI
EXPOSE 8000

# Default to Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]
