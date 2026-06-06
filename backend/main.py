from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Portfolio Risk Simulator is running"}