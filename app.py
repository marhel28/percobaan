from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Halo dari FastAPI di Vercel!"}

@app.get("/ping")
def ping():
    return {"status": "online"}