from fastapi import FastAPI
import os

app = FastAPI(title="RoE App")

@app.get("/")
def root():
    return {"name": "RoE App", "status": "ok"}

@app.get("/health")
def health():
    return {
        "ok": True,
        "version": os.getenv("APP_VERSION", "0.0.1"),
        "env": os.getenv("APP_ENV", "production")
    }
@app.get("/hello")
def hello(name: str = "traveler"):
    return {"message": f"Hello, {name}!"}
