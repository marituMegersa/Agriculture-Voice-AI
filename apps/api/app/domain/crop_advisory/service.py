from app.domain.crop_advisory.engine import CropDiagnosticEngine
from app.domain.crop_advisory.schemas import VoiceDiagnosticRequest, VoiceDiagnosticResponse

class CropAdvisoryService:
    @staticmethod
    def diagnose_voice_input(req: VoiceDiagnosticRequest) -> VoiceDiagnosticResponse:
        res = CropDiagnosticEngine.diagnose_transcript(
            transcript=req.voice_transcript,
            crop_type=req.crop_type,
            language=req.language
        )
        return VoiceDiagnosticResponse(
            farmer_id=req.farmer_id,
            crop_type=req.crop_type,
            diagnosis=res["diagnosis"],
            confidence=res["confidence"],
            recommended_treatment=res["recommended_treatment"],
            recommended_fertilizer=res["recommended_fertilizer"]
        )
