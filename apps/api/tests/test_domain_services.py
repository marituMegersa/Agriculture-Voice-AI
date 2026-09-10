def test_crop_advisory_model_instantiation():
    from app.domain.crop_advisory.models import CropAdvisoryRecord
    rec = CropAdvisoryRecord(id="REC-TEST-01")
    assert rec.id == "REC-TEST-01"

def test_crop_advisory_schema_validation():
    from app.domain.crop_advisory.schemas import CropAdvisoryResponse
    res = CropAdvisoryResponse(id="REC-TEST-01", status="COMPLETED", summary="Test", confidence_score=0.99, created_at="2026-09-10T16:00:00Z")
    assert res.status == "COMPLETED"
