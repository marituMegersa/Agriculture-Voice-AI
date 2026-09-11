import pytest
from app.services.domain import CropAdvisoryService
from app.repositories.domain import CropAdvisoryRepository
from app.schemas.domain import VoiceDiagnosticRequest

class MockSession:
    def add(self, obj): pass
    async def commit(self): pass
    async def refresh(self, obj): pass

@pytest.mark.asyncio
async def test_amharic_yellow_rust_voice_diagnostic():
    service = CropAdvisoryService(CropAdvisoryRepository(MockSession()))
    req = VoiceDiagnosticRequest(
        farmer_id="FARMER-882",
        crop_type="Wheat",
        voice_transcript="እህሌ ቢጫ ዝገት ምልክት አሳይቷል",
        language="Amharic"
    )
    res = await service.diagnose_voice_input(req)
    assert "Yellow Rust" in res.diagnosis
    assert res.confidence == 0.95
    assert "Propiconazole" in res.recommended_treatment

@pytest.mark.asyncio
async def test_early_blight_diagnostic():
    service = CropAdvisoryService(CropAdvisoryRepository(MockSession()))
    req = VoiceDiagnosticRequest(
        farmer_id="FARMER-883",
        crop_type="Potato",
        voice_transcript="Leaf spotting observed",
        language="English"
    )
    res = await service.diagnose_voice_input(req)
    assert "Early Blight" in res.diagnosis
    assert "Mancozeb" in res.recommended_treatment
