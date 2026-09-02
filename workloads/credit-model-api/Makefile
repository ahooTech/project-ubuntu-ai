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