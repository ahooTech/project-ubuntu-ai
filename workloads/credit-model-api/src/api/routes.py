from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram
from opentelemetry import trace

from src.models.credit_model import get_model
from src.config.settings import get_settings

router = APIRouter()
settings = get_settings()
model = get_model(settings.MODEL_VERSION)
tracer = trace.get_tracer(__name__)

# --- API Key Security (Applied ONLY to specific routes) ---
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "afribank-secure-platform-key-123":
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key

# --- Custom AI Platform Metrics ---
CREDIT_PREDICTIONS_TOTAL = Counter(
    'afribank_credit_predictions_total', 
    'Total number of credit score predictions',
    ['decision'] # Labels: 'Approved' or 'Declined'
)

PREDICTION_LATENCY = Histogram(
    'afribank_prediction_latency_seconds', 
    'Time taken to process a credit prediction'
)

# --- Request/Response Models ---
class CreditRequest(BaseModel):
    applicant_id: str = Field(..., description="Unique ID for the applicant")
    annual_income: float = Field(..., gt=0, description="Annual income in ZAR")
    monthly_debt: float = Field(..., ge=0, description="Monthly debt obligations in ZAR")
    credit_history_years: int = Field(..., ge=0, le=50, description="Years of credit history")

class CreditResponse(BaseModel):
    applicant_id: str
    credit_score: int
    decision: str
    model_version: str
    risk_factors: dict
    model_config = {"protected_namespaces": ()}

# --- Endpoints ---
@router.post("/predict", response_model=CreditResponse, tags=["Inference"], dependencies=[Depends(verify_api_key)])
async def predict_credit_score(request: CreditRequest):
    """
    Evaluate creditworthiness for a given applicant.
    Requires valid API Key.
    """
    with tracer.start_as_current_span("credit_prediction_inference"):
        with PREDICTION_LATENCY.time(): # Track latency
            try:
                result = model.predict(
                    annual_income=request.annual_income,
                    monthly_debt=request.monthly_debt,
                    credit_history_years=request.credit_history_years
                )
                
                # Track custom business metric
                CREDIT_PREDICTIONS_TOTAL.labels(decision=result['decision']).inc()
                
                return CreditResponse(
                    applicant_id=request.applicant_id,
                    **result
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Model inference failed: {str(e)}")

@router.get("/health", tags=["Health"])
async def health_check():
    # NO security dependency here. Kubernetes needs this to be public.
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "model_version": settings.MODEL_VERSION
    }