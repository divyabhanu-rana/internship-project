from fastapi import FastAPI
from backend.app.api.generate import router as generate_router

app = FastAPI(title="AI Material Generator")

app.include_router(generate_router, prefix="/api", tags = ["generate"])

@app.get("/")
def root():
     return {"message": "Backend is running!"}