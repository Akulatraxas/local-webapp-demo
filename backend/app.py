from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/api")
def root():
    return {
        "message": "Hello from backend",
        "environment": os.getenv("APP_ENV", "not-set"),
        "apikey": os.getenv("API_KEY", "not-set"),
        "akudesires": os.getenv("AKUDESIRES", "not-set"),
        "aku_from_infisical": os.getenv("AKU_FROM_INFISICAL", "not-set"),
    }
