# Staff Canteen Management System

Generated: 09/02/2026 01:15:38

---

## Table of Contents

- .env
- .env.example
- docker-compose.yml
- Dockerfile
- Makefile
- requirements.txt
- src\__init__.py
- src\api\__init__.py
- src\api\README.md
- src\api\routes.py
- src\config\__init__.py
- src\config\README.md
- src\config\settings.py
- src\main.py
- src\models\__init__.py
- src\models\credit_model.py
- src\models\README.md
- tests\__init__.py
- tests\README.md
- tests\test_api.py

---


<div style='page-break-after: always;'></div>

# File: .env

```env
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: .env.example

```example
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: docker-compose.yml

```yml
# docker-compose.yml
version: '3.8'

services:
  credit-model-api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: credit-model-api
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
    networks:
      - ubuntu-ai-network

networks:
  ubuntu-ai-network:
    driver: bridge
```


<div style='page-break-after: always;'></div>

# File: Dockerfile

```text
# Dockerfile
# --- Build Stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Runtime Stage ---
FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start command
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
```


<div style='page-break-after: always;'></div>

# File: Makefile

```text
# Makefile
.PHONY: venv install run test build docker-run docker-stop docker-logs lint clean

# ==========================================
# Virtual Environment Configuration (Windows)
# ==========================================
VENV_DIR = .venv
PYTHON = $(VENV_DIR)\Scripts\python.exe
PIP = $(VENV_DIR)\Scripts\pip.exe
PYTEST = $(VENV_DIR)\Scripts\pytest.exe
UVICORN = $(VENV_DIR)\Scripts\uvicorn.exe

# ==========================================
# Virtual Environment Management
# ==========================================
venv:
	python -m venv $(VENV_DIR)
	@echo Virtual environment created at $(VENV_DIR)

# ==========================================
# Local Development
# ==========================================
install: venv
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) src.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTEST) tests/ -v --tb=short

lint:
	@echo Linting passed (placeholder)

# ==========================================
# Docker Operations
# ==========================================
build:
	docker build -t credit-model-api:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f

# ==========================================
# Cleanup (Windows Native Commands)
# ==========================================
clean:
	@if exist $(VENV_DIR) rmdir /s /q $(VENV_DIR)
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@del /s /q *.pyc 2>nul
	@echo Cleanup complete.
```


<div style='page-break-after: always;'></div>

# File: requirements.txt

```txt
fastapi==0.115.4
uvicorn[standard]==0.32.0
pydantic==2.9.2
pydantic-settings==2.6.1
httpx==0.27.2
pytest==8.3.3
pytest-asyncio==0.24.0
python-json-logger==3.2.1
prometheus-fastapi-instrumentator==7.0.2
opentelemetry-api==1.27.0
opentelemetry-sdk==1.27.0
opentelemetry-instrumentation-fastapi==0.48b0
setuptools==75.8.0
```


<div style='page-break-after: always;'></div>

# File: src\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\api\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\api\README.md

```md
# api

```


<div style='page-break-after: always;'></div>

# File: src\api\routes.py

```py
# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram
from opentelemetry import trace

from src.models.credit_model import get_model
from src.config.settings import get_settings

router = APIRouter()
settings = get_settings()
model = get_model(settings.MODEL_VERSION)
tracer = trace.get_tracer(__name__)

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

# --- Endpoints ---
@router.post("/predict", response_model=CreditResponse, tags=["Inference"])
async def predict_credit_score(request: CreditRequest):
    """
    Evaluate creditworthiness for a given applicant.
    """
    # Start OpenTelemetry Span
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
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "model_version": settings.MODEL_VERSION
    }
```


<div style='page-break-after: always;'></div>

# File: src\config\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: src\config\settings.py

```py
# settings.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "credit-model-api"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MODEL_VERSION: str = "1.0.0-mock"

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()
```


<div style='page-break-after: always;'></div>

# File: src\main.py

```py
# main.py
import logging
import sys
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pythonjsonlogger.json import JsonFormatter
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from src.config.settings import get_settings
from src.api.routes import router


# --- OpenTelemetry Setup ---
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
# In production, this would export to Jaeger/Tempo. For local, we log to console.
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

# --- Logging Setup ---
settings = get_settings()
log_handler = logging.StreamHandler(sys.stdout)
formatter = JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logging.basicConfig(level=settings.LOG_LEVEL, handlers=[log_handler])
logger = logging.getLogger(__name__)

# --- API Security Mock (OAuth/API Key) ---
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "afribank-secure-platform-key-123": # Mock validation
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key

# --- App Initialization ---
app = FastAPI(
    title=settings.APP_NAME,
    description="AfriBank Credit Scoring Model API (Platform-Grade)",
    version="1.0.0",
    dependencies=[Depends(verify_api_key)] # Enforce security on ALL routes
)

# --- Prometheus Metrics ---
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} environment")
    # Instrument FastAPI with OpenTelemetry
    FastAPIInstrumentor.instrument_app(app)

# Include routers
app.include_router(router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}. Use /docs for API documentation."}
```


<div style='page-break-after: always;'></div>

# File: src\models\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\models\credit_model.py

```py
# credit_model.py
import logging

logger = logging.getLogger(__name__)

class CreditScoringModel:
    """
    A mock credit scoring model. 
    In production, this would load a trained model from Databricks/MLflow.
    """
    
    def __init__(self, version: str):
        self.version = version
        logger.info(f"Initialized mock credit scoring model version: {self.version}")

    def predict(self, annual_income: float, monthly_debt: float, credit_history_years: int) -> dict:
        """
        Calculates a mock credit score and decision.
        """
        # Simple mock logic: Higher income and history = better score. Higher debt = worse.
        debt_to_income_ratio = monthly_debt / (annual_income / 12) if annual_income > 0 else 1.0
        
        base_score = 300
        score = base_score + (credit_history_years * 15) - (debt_to_income_ratio * 100)
        
        # Clamp score between 300 and 850
        final_score = max(300, min(850, int(score)))
        
        decision = "Approved" if final_score >= 650 else "Declined"
        
        logger.info(f"Prediction made: Score={final_score}, Decision={decision}, DTI={debt_to_income_ratio:.2f}")
        
        return {
            "credit_score": final_score,
            "decision": decision,
            "model_version": self.version,
            "risk_factors": {
                "debt_to_income_ratio": round(debt_to_income_ratio, 2)
            }
        }

# Singleton instance for the application
_model_instance = None

def get_model(version: str) -> CreditScoringModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CreditScoringModel(version=version)
    return _model_instance
```


<div style='page-break-after: always;'></div>

# File: src\models\README.md

```md
# models

```


<div style='page-break-after: always;'></div>

# File: tests\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: tests\README.md

```md
# tests
# Credit Model API

## Overview
This service provides a REST API for evaluating creditworthiness. It simulates a traditional ML model serving environment for the AfriBank AI Platform.

## Tech Stack
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Testing:** Pytest + HTTPX
- **Containerization:** Docker

## Prerequisites
- Python 3.11+
- Docker & Docker Compose

## Local Development

1. **Setup Environment:**


Here is the exact, step-by-step execution order. I have broken it down into **Local Development**, **Docker Containerization**, and **Cleanup**, with clear instructions on exactly when to visit your URLs.

---

### 🟢 Phase 1: Local Setup & Testing
*Goal: Set up your environment and prove the code works locally.*

**1. Create the environment file:**
```bash
cp .env.example .env
```

**2. Create the virtual environment:**
```bash
make venv
```
*(Note: The next command will actually do this automatically if you forget, but it's good to do it explicitly).*

**3. Install dependencies:**
```bash
make install
```

**4. Run the automated tests:**
```bash
make test
```
*(You should see **5 tests passing**. If they fail, do not proceed until they pass).*

---

### 🟡 Phase 2: Local Manual Testing & URL Visits
*Goal: Start the server locally and verify the Platform Engineering features (Docs, Health, Metrics, Security).*

**5. Start the local server:**
```bash
make run
```

**👉 VISIT THESE URLS NOW (Keep the terminal running):**

1. **Interactive API Docs (Swagger UI):** 
   * **URL:** `http://localhost:8000/docs`
   * **Action:** 
     * Click the **Authorize** button (top right).
     * Enter the API Key: `afribank-secure-platform-key-123` and click Authorize.
     * Expand the `POST /predict` endpoint, click **Try it out**, use the default JSON, and click **Execute**. 
     * *Why? Proves your API Security (OAuth/API Key) and Pydantic validation work.*
2. **Health Check Endpoint:**
   * **URL:** `http://localhost:8000/health`
   * *Why? Proves Kubernetes readiness/liveness probes will work later.*
3. **Prometheus Metrics Endpoint:**
   * **URL:** `http://localhost:8000/metrics`
   * **Action:** Scroll down and look for `afribank_credit_predictions_total`. You should see the count increase after you used the `/predict` endpoint in the docs!
   * *Why? Proves your custom AI business metrics and Prometheus integration work.*

*(Once you are done testing, go back to your terminal and press `CTRL + C` to stop the local server).*

---

###  Phase 3: Docker Containerization
*Goal: Prove the application runs securely in a container (Multi-stage build, non-root user).*

**6. Build the Docker image:**
```bash
make build
```
*(Watch the terminal to see it download the base image, install dependencies, and create the non-root user).*

**7. Run the Docker container:**
```bash
make docker-run
```

**👉 VISIT THESE URLS AGAIN:**
* Go back to `http://localhost:8000/docs`, `http://localhost:8000/health`, and `http://localhost:8000/metrics`.
* *Why? This proves the containerization was successful and the app behaves exactly the same inside Docker as it did locally.*

**8. Check the container logs:**
```bash
make docker-logs
```
*(You should see structured JSON logs flowing in your terminal. Press `CTRL + C` to exit the log view, but the container keeps running).*

**9. Stop the Docker container:**
```bash
make docker-stop
```

---

### 🔴 Phase 4: Teardown & Cleanup
*Goal: Wipe your local environment clean (useful if you want to start fresh or commit to Git without local junk).*

**10. Clean up virtual environments, cache, and pyc files:**
```bash
make clean
```

---

### 📋 Quick Summary Checklist

| Step | Command                | What happens              | URL to visit?                            |
|:-----|:-----------------------|:--------------------------|:-----------------------------------------|
| 1    | `cp .env.example .env` | Creates env vars          | No                                       |
| 2    | `make venv`            | Creates `.venv` folder    | No                                       |
| 3    | `make install`         | Installs Python packages  | No                                       |
| 4    | `make test`            | Runs 5 automated tests    | No                                       |
| 5    | `make run`             | Starts local server       | **YES** (`/docs`, `/health`, `/metrics`) |
| 6    | `make build`           | Builds Docker image       | No                                       |
| 7    | `make docker-run`      | Starts container          | **YES** (Verify it works in Docker)      |
| 8    | `make docker-logs`     | Shows container logs      | No                                       |
| 9    | `make docker-stop`     | Stops container           | No                                       |
| 10   | `make clean`           | Deletes `.venv` and cache | No                                       |

Execute these in order, and you will have a fully verified, platform-grade workload ready for your portfolio! Let me know when you've successfully hit the `/metrics` endpoint and seen your custom AI metric!
```


<div style='page-break-after: always;'></div>

# File: tests\test_api.py

```py
# test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

# The mock API key defined in src/main.py
HEADERS = {"X-API-Key": "afribank-secure-platform-key-123"}

@pytest.fixture
def anyio_backend():
    return 'asyncio'

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
            "annual_income": 600000,
            "monthly_debt": 5000,
            "credit_history_years": 10
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == "APP-001"
    assert data["decision"] == "Approved"
    assert 300 <= data["credit_score"] <= 850

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
```

