from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}