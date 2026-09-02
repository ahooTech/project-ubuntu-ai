#test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app
from opentelemetry import trace

# The mock API key defined in src/main.py
HEADERS = {"X-API-Key": "afribank-secure-platform-key-123"}

@pytest.fixture
def anyio_backend():
    return 'asyncio'

# Gracefully shut down OpenTelemetry to prevent the "closed file" error on exit
@pytest.fixture(autouse=True)
def cleanup_otel():
    yield
    provider = trace.get_tracer_provider()
    if hasattr(provider, 'shutdown'):
        provider.shutdown()

@pytest.mark.anyio
async def test_health_check():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health", headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "model_version" in data

@pytest.mark.anyio
async def test_predict_approved():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-001",
            "annual_income": 1200000,  # Higher income
            "monthly_debt": 2000,      # Lower debt
            "credit_history_years": 30 # Longer history
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == "APP-001"
    assert data["decision"] == "Approved"
    assert 650 <= data["credit_score"] <= 850

@pytest.mark.anyio
async def test_predict_declined():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-002",
            "annual_income": 120000,
            "monthly_debt": 9000,
            "credit_history_years": 1
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "Declined"

@pytest.mark.anyio
async def test_predict_validation_error():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-003",
            "annual_income": -500, # Invalid: must be > 0
            "monthly_debt": 1000,
            "credit_history_years": 5
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 422 # Unprocessable Entity

@pytest.mark.anyio
async def test_unauthorized_access():
    """
    Proves our API Security is working (Absa JD: API Security, OAuth 2.0).
    Requests without the valid X-API-Key header must be rejected.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-004",
            "annual_income": 100000,
            "monthly_debt": 1000,
            "credit_history_years": 1
        }
        # Intentionally sending NO HEADERS
        response = await ac.post("/predict", json=payload)
    
    assert response.status_code == 403 # Forbidden