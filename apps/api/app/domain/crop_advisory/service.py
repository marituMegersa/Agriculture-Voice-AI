from typing import Dict, Any
import uuid

class CropAdvisoryService:
    @staticmethod
    def diagnose_crop(farmer_id: str, crop_type: str, symptom_text: str, language: str = "am") -> Dict[str, Any]:
        disease = "Nitrogen Deficiency / Wheat Rust" if "yellow" in symptom_text.lower() or "ብጫ" in symptom_text else "Early Blight"
        treatment = "Apply Urea fertilizer (50kg/ha) and fungicide spray within 5 days."
        return {
            "consultation_id": f"ADV-{uuid.uuid4().hex[:8]}",
            "farmer_id": farmer_id,
            "crop_type": crop_type,
            "detected_disease": disease,
            "recommended_treatment": treatment,
            "language": language
        }
