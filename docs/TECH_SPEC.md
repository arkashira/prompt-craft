# TECH_SPEC.md – Prompt‑Craft

---

## 1. Overview

**Prompt‑Craft** is a SaaS platform that enables data scientists, product managers, and developers to design, test, and iterate LLM prompts at scale.  
The system exposes a web UI, a REST/GraphQL API, and a background job pipeline that:

1. **Stores** prompt templates and test cases in a relational DB.  
2. **Executes** prompts against a production‑grade inference engine (vLLM).  
3. **Collects** metrics (latency, token usage, success rate) and stores them in a time‑series store.  
4. **Provides** analytics dashboards and export hooks.

The platform is built to integrate seamlessly with the existing Axentx ecosystem (shared pgvector brain, data‑pipeline, and CI/CD).

---

## 2. Architecture

```
┌───────────────────────┐
│  Front‑end (React)    │
│  - Prompt editor      │
│  - Test runner UI     │
│  - Analytics dashboard│
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  API Gateway (FastAPI)│
│  - Auth (OAuth2)      │
│  - Rate‑limit         │
│  - Request/Response   │
└───────┬───────┬───────┘
        │       │
        ▼       ▼
┌───────────────┐   ┌───────────────────────┐
│  Prompt Service│   │  Metrics Service        │
│  - CRUD        │   │  - Ingest metrics       │
│  - Validation  │   │  - Store in TimescaleDB│
└───────┬───────┘   └───────────────┬─────────┘
        │                       │
        ▼                       ▼
┌───────────────────────┐   ┌───────────────────────┐
│  vLLM Inference Layer │   │  PostgreSQL (pgvector)│
│  - vLLM Docker image   │   │  - Prompt & test data  │
│  - Model registry      │   │  - Prompt embeddings   │
└───────┬───────┬───────┘   └───────┬───────┬───────┘
        │       │               │       │
        ▼       ▼               ▼       ▼
┌───────────────────────┐   ┌───────────────────────┐
│  Background Workers   │   │  Redis (Task Queue)   │
│  - Celery (RQ)         │   │  - Job scheduling     │
│  - Run prompt tests   │   │  - Pub/Sub            │
└───────────────────────┘   └───────────────────────┘
```

### 2.1 Front‑end

* **Framework**: React 18 + Vite  
* **State**: Redux Toolkit + RTK Query  
* **UI Library**: MUI v5  
* **Auth**: OAuth2 via Keycloak (SAML/OIDC)  

### 2.2 API Layer

* **Framework**: FastAPI 0.110  
* **Auth**: OAuth2 JWT, scopes for `prompt:read`, `prompt:write`, `metrics:read`  
* **Rate‑limit**: `slowapi` (Redis backend)  
* **Docs**: OpenAPI + GraphQL introspection  

### 2.3 Prompt Service

* **Endpoints**  
  * `POST /prompts` – create prompt template  
  * `GET /prompts/{id}` – retrieve prompt  
  * `PUT /prompts/{id}` – update prompt  
  * `DELETE /prompts/{id}` – delete prompt  
  * `POST /prompts/{id}/tests` – add test case  
  * `GET /prompts/{id}/tests` – list tests  
  * `POST /prompts/{id}/run` – trigger test run  

* **Validation** – schema validation via Pydantic, prompt syntax check (LLM‑friendly formatting).  

### 2.4 Metrics Service

* **Ingest** – Celery workers consume `prompt_run` events, parse logs, compute metrics.  
* **Store** – TimescaleDB (PostgreSQL extension) for high‑cardinality time series.  
* **Query** – PromQL‑style queries via Grafana integration.  

### 2.5 vLLM Inference Layer

* **Container** – `vllm-project/vllm:latest` with GPU support.  
* **Model Registry** – Configurable via `models.yaml`.  
* **Endpoint** – `/vllm/infer` (FastAPI proxy).  
* **Batching** – vLLM’s native batching, configurable `max_batch_size`.  

### 2.6 Background Workers

* **Framework**: Celery 5 + Redis broker.  
* **Jobs** – `run_prompt_test`, `refresh_embeddings`.  
* **Retry** – exponential backoff, max 5 attempts.  

### 2.7 Data Store

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `prompts` | Prompt templates | `id`, `name`, `content`, `created_at`, `updated_at` |
| `tests` | Test cases | `id`, `prompt_id`, `input`, `expected_output`, `created_at` |
| `prompt_runs` | Run metadata | `id`, `prompt_id`, `test_id`, `status`, `start_ts`, `end_ts` |
| `metrics` | Time‑series metrics | `run_id`, `timestamp`, `latency_ms`, `tokens_in`, `tokens_out` |
| `embeddings` | pgvector embeddings | `prompt_id`, `embedding vector` |

All tables are in PostgreSQL 15 with `pgvector` extension enabled.

---

## 3. Data Model

```sql
-- prompts
CREATE TABLE prompts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- tests
CREATE TABLE tests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prompt_id UUID REFERENCES prompts(id) ON DELETE CASCADE,
  input TEXT NOT NULL,
  expected_output TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- prompt_runs
CREATE TABLE prompt_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prompt_id UUID REFERENCES prompts(id),
  test_id UUID REFERENCES tests(id),
  status TEXT NOT NULL, -- queued, running, succeeded, failed
  start_ts TIMESTAMPTZ,
  end_ts TIMESTAMPTZ,
  output TEXT
);

-- metrics
CREATE TABLE metrics (
  run_id UUID REFERENCES prompt_runs(id),
  timestamp TIMESTAMPTZ NOT NULL,
  latency_ms INT,
  tokens_in INT,
  tokens_out INT,
  PRIMARY KEY (run_id, timestamp)
);

-- embeddings
CREATE TABLE embeddings (
  prompt_id UUID PRIMARY KEY REFERENCES prompts(id),
  embedding vector(1536) -- 1536-dim for OpenAI embeddings
);
```

---

## 4. Key APIs / Interfaces

| API | Method | Path | Description |
|-----|--------|------|-------------|
| Create Prompt | POST | `/prompts` | Create a new prompt template. |
| Get Prompt | GET | `/prompts/{id}` | Retrieve prompt metadata. |
| Update Prompt | PUT | `/prompts/{id}` | Update prompt content. |
| Delete Prompt | DELETE | `/prompts/{id}` | Delete prompt. |
| Add Test | POST | `/prompts/{id}/tests` | Add a test case to a prompt. |
| List Tests | GET | `/prompts/{id}/tests` | List all tests for a prompt. |
| Run Test | POST | `/prompts/{id}/run` | Trigger a background job to run all tests. |
| Get Run Status | GET | `/runs/{run_id}` | Poll status and output. |
| Metrics Query | GET | `/metrics?run_id={}` | Retrieve time‑series metrics. |
| vLLM Inference | POST | `/vllm/infer` | Proxy to vLLM inference endpoint. |

All endpoints return JSON, use standard HTTP status codes, and include pagination where applicable.

---

## 5. Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Front‑end | React, Vite, MUI, Redux Toolkit | 2026‑06 |
| API | FastAPI, Pydantic | 0.110 |
| Auth | Keycloak, OAuth2 JWT | 23.0 |
| Inference | vLLM (vllm-project/vllm) | 0.5 |
| DB | PostgreSQL 15 + pgvector | 15.2 |
| Time‑Series | TimescaleDB | 2.10 |
| Queue | Redis 7, Celery 5 | 7.2 |
| Container | Docker, Docker‑Compose | 24.0 |
| CI/CD | GitHub Actions, ArgoCD | - |
| Monitoring | Prometheus, Grafana | - |

---

## 6. Dependencies

| Category | Package | Purpose |
|----------|---------|---------|
| Core | `fastapi`, `uvicorn`, `pydantic` | API framework |
| Auth | `python-jose`, `fastapi-security` | JWT handling |
| DB | `asyncpg`, `sqlalchemy`, `pgvector` | PostgreSQL access |
| Inference | `vllm`, `transformers` | LLM inference |
| Queue | `celery`, `redis` | Background jobs |
| Metrics | `prometheus-client`, `timescale` | Time‑series storage |
| Front‑end | `react`, `@mui/material`, `redux-toolkit` | UI |
| Dev | `pytest`, `black`, `isort` | Testing & linting |

All dependencies are pinned in `pyproject.toml` and `package.json`. Docker images are built via multi‑stage builds.

---

## 7. Deployment

### 7.1 Local Development

```bash
# Clone repo
git clone https://github.com/arkashira/prompt-craft.git
cd prompt-craft

# Build & run
docker compose -f docker-compose.dev.yml up --build
```

* **Frontend**: `http://localhost:3000`  
* **API**: `http://localhost:8000`  
* **vLLM**: `http://localhost:8001`  

### 7.2 Production

1. **Infrastructure** – Kubernetes cluster (EKS/GKE) with managed RDS (PostgreSQL + Timescale) and Elasticache (Redis).  
2. **Helm Charts** – `prompt-craft-helm` contains deployments for API, frontend, vLLM, workers, and monitoring.  
3. **CI/CD** – GitHub Actions build Docker images, push to ECR/GCR, trigger ArgoCD sync.  
4. **Secrets** – Managed via Vault; Keycloak credentials, DB passwords, JWT secrets.  
5. **Scaling** –  
   * API: Horizontal Pod Autoscaler (CPU 70%)  
   * Workers: Scale based on Redis queue length  
   * vLLM: GPU nodes (NVIDIA A10G) with pod affinity to GPU resources  

### 7.3 Observability

* **Logs** – Structured JSON to Loki.  
* **Metrics** – Prometheus scrape from FastAPI `/metrics`.  
* **Tracing** – OpenTelemetry, Jaeger.  
* **Dashboards** – Grafana dashboards for prompt latency, token usage, error rates.

---

## 8. Security & Compliance

* **Data Encryption** – TLS for all traffic, AES‑256 at rest for DB.  
* **RBAC** – OAuth2 scopes, Keycloak groups.  
* **Audit** – Log all CRUD operations with user ID.  
* **GDPR** – Data retention policy: keep metrics for 90 days, prompts for 1 year.  

---

## 9. Future Enhancements

1. **Prompt Auto‑generation** – Integrate with GPT‑4 fine‑tuning for template suggestions.  
2. **A/B Testing** – Compare prompt variants in live traffic.  
3. **Marketplace** – Publish vetted prompts to Axentx brain.  
4. **Multi‑model Support** – Add Anthropic, Cohere backends.  

---

## 10. Contact & Maintenance

| Role | Contact |
|------|---------|
| Product Owner | alice@axentx.com |
| Lead Engineer | bob@axentx.com |
| Ops Lead | carol@axentx.com |

All code is under the `arkashira` GitHub organization. Please refer to the repository’s `CONTRIBUTING.md` for contribution guidelines.
