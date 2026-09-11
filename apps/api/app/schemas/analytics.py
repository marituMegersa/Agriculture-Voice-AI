from pydantic import BaseModel, Field
from typing import Dict, List

class CropAdvisoryAnalyticsResponse(BaseModel):
    total_diagnostics_run: int = Field(..., example=840)
    yellow_rust_cases: int = Field(..., example=310)
    early_blight_cases: int = Field(..., example=530)
    amharic_query_pct: float = Field(..., example=88.5)
    most_affected_crops: Dict[str, int] = Field(..., example={"Wheat": 420, "Maize": 260, "Teff": 160})
