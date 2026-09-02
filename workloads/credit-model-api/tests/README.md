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


```
curl.exe -X POST http://localhost:8000/predict `
  -H "Content-Type: application/json" `
  -H "X-API-Key: afribank-secure-platform-key-123" `
  -d '{\"applicant_id\": \"APP-999\", \"annual_income\": 500000, \"monthly_debt\": 4000, \"credit_history_years\": 8}'

```

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