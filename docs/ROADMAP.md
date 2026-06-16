# Roadmap – prompt‑craft

## Vision
**prompt‑craft** is a SaaS platform that lets data scientists, product managers, and developers design, test, and iterate LLM prompts at scale.  
We aim to become the go‑to prompt‑engineering hub for enterprises that need high‑quality, reproducible prompts for production workloads.

---

## 1. MVP – Launch Milestone (Q3 2026)

| # | Feature | Owner | Acceptance Criteria | Notes |
|---|---------|-------|---------------------|-------|
| 1 | **Prompt Editor** – WYSIWYG editor with syntax highlighting, linting, and real‑time preview | Front‑end | Editor loads in <2 s, supports Markdown & JSON, shows live LLM response | Uses Monaco editor; integrates with vLLM for inference |
| 2 | **Prompt Library** – CRUD, tagging, versioning, and sharing | Backend | Users can create, read, update, delete prompts; version history visible; shareable links | Store in PostgreSQL + pgvector for semantic search |
| 3 | **Inference Engine** – vLLM integration for fast, batched prompt evaluation | Backend | 100 req/s throughput, latency <200 ms for 1‑token prompts | Containerized vLLM, autoscaling on Kubernetes |
| 4 | **Result Analytics** – Scorecard (BLEU, ROUGE, custom metrics), heatmaps, and export | Backend + Front‑end | Users can view metrics per run, filter by prompt, export CSV | Metrics computed via HuggingFace datasets |
| 5 | **User Management & Billing** – OAuth2, role‑based access, subscription plans | Backend | Users sign up via Google, can create teams, view invoices | Stripe integration |
| 6 | **CI/CD Pipeline** – Automated tests, linting, deployment to staging & prod | DevOps | Every PR triggers tests, builds, and auto‑deploys to staging | GitHub Actions + ArgoCD |
| 7 | **Documentation & Onboarding** – Interactive tour, API docs, sample prompts | Front‑end | New users complete tour in <5 min, API docs available | Use Docusaurus |

**MVP‑Critical**: 1–5.  
Feature 6 is essential for reliability, 7 is critical for adoption.

---

## 2. v1 – Feature‑Rich Platform (Q4 2026 – Q1 2027)

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **Prompt Collaboration** | Real‑time co‑editing, comment threads, merge conflicts | Front‑end | Multiple users edit same prompt simultaneously, conflict resolution UI |
| **Advanced Metrics** | Human‑in‑the‑loop scoring, A/B testing, drift detection | Backend | Ability to run A/B tests, track performance over time, alert on drift |
| **Template Marketplace** | Pre‑built prompt templates, rating system, import/export | Front‑end | Users can browse, rate, and import templates; marketplace API |
| **Custom Model Integration** | Plug‑in SDK for custom LLMs, model registry | Backend | Users can register their own models, switch between them in the editor |
| **Security & Compliance** | Data encryption at rest, GDPR compliance, audit logs | DevOps | All data encrypted, logs retained 12 months, audit trail UI |
| **Performance Optimizations** | Caching layer, token‑budget estimator, batch scheduling | Backend | Cache hit rate >70 %, token estimator accuracy ±5 % |

---

## 3. v2 – Enterprise‑Ready & AI‑Powered (Q2 2027 – Q4 2027)

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **AI‑Assisted Prompt Generation** | GPT‑style auto‑completion, suggestion engine, semantic search | ML | Suggestion accuracy >80 % for common patterns, search recall >90 % |
| **Workflow Automation** | Triggered runs, webhook integrations, CI hooks | Backend | Users can set up webhooks, integrate with GitHub Actions, Slack |
| **Analytics Dashboard** | Custom dashboards, KPI tracking, alerts | Front‑end | Users create dashboards, set thresholds, receive email alerts |
| **Marketplace Expansion** | Third‑party extensions, API marketplace | Front‑end | External developers can publish extensions, users can install |
| **Scalability Enhancements** | Multi‑region deployment, autoscaling, cost‑optimization | DevOps | 99.9 % uptime, cost per inference < $0.0001 |
| **Governance & Policy** | Prompt approval workflows, role‑based policy engine | Backend | Admins can enforce prompt policies, audit trail of approvals |

---

## 4. Continuous Improvement Loop

| Activity | Frequency | Owner |
|----------|-----------|-------|
| **User Feedback Sessions** | Monthly | Product |
| **Metric Review (KPIs)** | Weekly | Analytics |
| **Security Audits** | Quarterly | Security |
| **Model Performance Benchmarking** | Bi‑monthly | ML |
| **Roadmap Refinement** | Quarterly | Executive |

---

## 5. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Monthly Active Users (MAU)** | 10k | Mixpanel |
| **Prompt Library Growth** | 5k prompts | PostgreSQL |
| **Inference Latency** | <200 ms | Prometheus |
| **Revenue** | $500k ARR | Stripe |
| **Customer Satisfaction (CSAT)** | ≥90 % | SurveyMonkey |

---

### Key Dependencies

- **vLLM** for inference (already verified repo: `vllm-project/vllm`).
- **pgvector** for semantic search (shared company brain).
- **GitHub Actions** for CI/CD (runbook reference).
- **Stripe** for billing (standard SaaS stack).

---

### Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| **Model drift** | Continuous monitoring, drift alerts |
| **Data privacy** | End‑to‑end encryption, GDPR compliance |
| **Scalability bottleneck** | Autoscaling, caching, multi‑region |
| **Feature creep** | Strict feature gate, MVP focus |

---

## Timeline Overview

```
Q3 2026  ── MVP Launch
Q4 2026  ── v1 Feature Rollout
Q1 2027  ── v1 Completion
Q2 2027  ── v2 Alpha
Q3 2027  ── v2 Beta
Q4 2027  ── v2 Full Release
```

---

*Prepared by the prompt‑craft Product & Engineering Lead*
