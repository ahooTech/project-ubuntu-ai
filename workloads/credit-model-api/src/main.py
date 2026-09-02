import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
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

# --- Lifespan Context Manager ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} environment")
    yield
    logger.info(f"Shutting down {settings.APP_NAME}")

# --- App Initialization ---
# NOTE: No global dependencies here. This ensures /health and /metrics remain PUBLIC 
# for Kubernetes probes and Prometheus scraping.
app = FastAPI(
    title=settings.APP_NAME,
    description="AfriBank Credit Scoring Model API (Platform-Grade)",
    version="1.0.0",
    lifespan=lifespan
)

# --- OpenTelemetry Instrumentation (MUST be outside lifespan, right after app creation) ---
FastAPIInstrumentor.instrument_app(app)

# --- Prometheus Metrics (Public for Prometheus scraping) ---
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Include routers (security is applied per-route inside routes.py)
app.include_router(router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}. Use /docs for API documentation."}