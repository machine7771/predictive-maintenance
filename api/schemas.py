from pydantic import BaseModel, Field
from typing import Optional, Literal


# -------------------------
# 1. SENSOR INPUT
# -------------------------

class SensorInput(BaseModel):

    temperature_mean: float = Field(..., description="Average temperature in Celsius")
    temperature_std: float = Field(..., ge=0, description="Temperature standard deviation")

    current_mean: float = Field(..., description="Average current in mA")
    current_std: float = Field(..., ge=0, description="Current standard deviation")

    vibration_rate: float = Field(
        ...,
        ge=0,
        le=1,
        description="Vibration event ratio"
    )


# -------------------------
# 2. AI PREDICTION OUTPUT
# -------------------------

class PredictionOutput(BaseModel):

    status: Literal[
        "NORMAL",
        "PREDICTED_ANOMALY",
        "ABNORMAL"
    ]

    anomaly_score: Optional[float] = None

    detection_method: Optional[str] = None

    individual_threshold_exceeded: bool = False

    multivariate_anomaly_detected: bool = False

    recommendation: str


# -------------------------
# 3. HEALTH RESPONSE
# -------------------------

class HealthResponse(BaseModel):

    status: str
    model_loaded: bool


# -------------------------
# 4. MODEL INFORMATION
# -------------------------

class ModelInfoResponse(BaseModel):

    model_version: Optional[str] = None
    trained_at: Optional[str] = None
    features: list[str] = []
