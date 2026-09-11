from typing import Dict, Any

class CropDiagnosticEngine:
    DIAGNOSTIC_RULES = {
        "rust": {
            "disease": "Yellow Rust (Puccinia striiformis)",
            "fungicide": "Apply Propiconazole fungicide at 0.5L/ha in early morning.",
            "fertilizer": "Urea: 100 kg/ha, DAP: 50 kg/ha",
            "confidence": 0.94
        },
        "blight": {
            "disease": "Early Blight (Alternaria solani)",
            "fungicide": "Apply Mancozeb 80% WP at 2.0 kg/ha every 7-10 days.",
            "fertilizer": "Compost: 5 tonnes/ha, Potassium Chloride: 40 kg/ha",
            "confidence": 0.91
        }
    }

    @classmethod
    def diagnose_transcript(cls, transcript: str, crop_type: str, language: str) -> Dict[str, Any]:
        text_lower = transcript.lower()
        if "ቢጫ" in transcript or "rust" in text_lower:
            key = "rust"
        else:
            key = "blight"
            
        rule = cls.DIAGNOSTIC_RULES[key]
        return {
            "diagnosis": rule["disease"],
            "confidence": rule["confidence"],
            "recommended_treatment": rule["fungicide"],
            "recommended_fertilizer": rule["fertilizer"],
            "language": language
        }
