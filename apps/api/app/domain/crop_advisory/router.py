from fastapi import APIRouter
from app.domain.crop_advisory.service import *

router = APIRouter(prefix="/api/v1/crop_advisory", tags=["Agriculture & Voice AI Advisory"])

@router.get("/status")
def get_domain_status():
    return {"status": "active", "domain": "Agriculture & Voice AI Advisory"}
