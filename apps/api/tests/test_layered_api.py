import pytest

def test_voice_diagnostic_payload():
    diag_data = {
        "farmer_id": "FARMER-991",
        "crop_type": "Wheat",
        "voice_transcript": "እህሌ ቢጫ ዝገት ምልክት አሳይቷል",
        "language": "Amharic"
    }
    assert "FARMER" in diag_data["farmer_id"]
    assert diag_data["language"] == "Amharic"
