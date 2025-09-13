from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"name":"RoE App","status":"ok"}
