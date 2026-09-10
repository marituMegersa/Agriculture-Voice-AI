from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.domain.crop_advisory.router import router as domain_router

app = FastAPI(title="Agriculture & Voice AI Advisory API", description="Multilingual Crop Diagnostic & Soil Advisor (Amharic / Afaan Oromo)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(domain_router)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Agriculture & Voice AI Advisory"}
