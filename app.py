import uvicorn
from fastapi import FastAPI

V = 100
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "===Hello World==="}

@app.get("/valeurv")
async def valeur_v():
    return {"message": f"La variable V est : {V}"}
