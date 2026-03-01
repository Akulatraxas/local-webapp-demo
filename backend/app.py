from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/api")
def root():
    return {
        "message": "Hello from backend",
        "environment": os.getenv("APP_ENV", "not-set")
    }
