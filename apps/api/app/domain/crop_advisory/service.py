from typing import Dict, Any
import uuid

class CropAdvisoryService:
    @staticmethod
    def diagnose_crop(farmer_id: str, crop_type: str, symptom_text: str, language: str = "am") -> Dict[str, Any]:
        if "yellow" in symptom_text.lower() or "ብጫ" in symptom_text or "boora" in symptom_text:
            disease = "Nitrogen Deficiency / Wheat Rust"
            treatment = "Apply Urea fertilizer (50kg/ha) and fungicide spray within 5 days."
        else:
            disease = "Early Blight / Fungal Spot"
            treatment = "Apply Copper-based fungicide spray and reduce overhead irrigation."

        translated_summary = "የሰብል በሽታ ምርመራ ውጤት፡ " + disease if language == "am" else "Qorannoo Dhibee Midhaanii: " + disease

        return {
            "consultation_id": f"ADV-{uuid.uuid4().hex[:8]}",
            "farmer_id": farmer_id,
            "crop_type": crop_type,
            "detected_disease": disease,
            "recommended_treatment": treatment,
            "localized_summary": translated_summary
        }
