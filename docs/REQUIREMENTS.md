# REQUIREMENTS.md

## 1. Overview

**Project**: `prompt-craft`  
**Type**: SaaS platform for crafting, testing, and refining LLM prompts.  
**Goal**: Enable users to create high‑quality prompts, evaluate them against target LLMs, and iterate quickly with analytics and versioning.

The product must integrate with Axentx’s existing infrastructure (shared BRAIN, data pipelines, and deployment tooling) and adhere to company standards for security, performance, and reliability.

---

## 2. Functional Requirements

| ID | Description | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR‑1** | **User Registration & Authentication** | Must | • OAuth2 + email‑password sign‑up<br>• MFA via TOTP<br>• Role‑based access (Admin, Editor, Viewer) |
| **FR‑2** | **Prompt Editor** | Must | • WYSIWYG editor with syntax highlighting for JSON, YAML, and plain text<br>• Auto‑completion for LLM instruction patterns<br>• Real‑time linting against prompt‑craft schema |
| **FR‑3** | **Prompt Versioning** | Must | • Git‑style commit history per prompt<br>• Branching and merging with conflict resolution UI |
| **FR‑4** | **LLM Integration** | Must | • Plug‑in architecture to support any LLM via Axentx inference engine (vLLM, SGLang, etc.)<br>• Ability to specify model, temperature, max tokens, etc. |
| **FR‑5** | **Prompt Testing** | Must | • Run prompt against selected LLM and display raw output<br>• Capture latency, token usage, and cost metrics |
| **FR‑6** | **Evaluation Metrics** | Must | • Compute BLEU, ROUGE, METEOR, and custom user‑defined metrics<br>• Visual comparison charts (heatmaps, line graphs) |
| **FR‑7** | **Collaboration** | Must | • Real‑time co‑editing (CRDT or OT)<br>• Comment threads tied to specific prompt lines |
| **FR‑8** | **Analytics Dashboard** | Must | • Global prompt performance metrics (avg. latency, cost, success rate)<br>• Exportable CSV/JSON reports |
| **FR‑9** | **Export/Import** | Must | • Export prompt in JSON/YAML<br>• Import prompts with validation against schema |
| **FR‑10** | **Audit Trail** | Must | • Immutable log of all changes with timestamps and user IDs |
| **FR‑11** | **API Access** | Should | • RESTful API for CRUD operations on prompts and tests<br>• Webhook support for test completion |
| **FR‑12** | **User Settings** | Should | • Personal preferences (theme, default model, notification settings) |
| **FR‑13** | **Scalability** | Should | • Auto‑scale compute resources for test runs based on queue depth |
| **FR‑14** | **Internationalization** | Should | • UI supports at least English, Spanish, and Chinese (UTF‑8) |
| **FR‑15** | **Accessibility** | Should | • WCAG 2.1 AA compliance for all UI components |

---

## 3. Non‑Functional Requirements

| ID | Category | Requirement | Acceptance Criteria |
|----|----------|-------------|---------------------|
| **NFR‑1** | Performance | <ul><li>Prompt editor latency < 50 ms for 5 kB content</li><li>Test run initiation < 2 s</li><li>Dashboard refresh < 1 s</li></ul> | Benchmarks on target hardware (AWS g4dn.xlarge) |
| **NFR‑2** | Security | <ul><li>All data encrypted at rest (AES‑256) and in transit (TLS 1.3)</li><li>Role‑based access enforced on API and UI</li><li>Audit logs tamper‑proof (hash chaining)</li></ul> | Pen‑test results, OWASP Top‑10 compliance |
| **NFR‑3** | Reliability | <ul><li>99.9 % uptime SLA for API</li><li>Graceful degradation: if LLM service down, queue retries with exponential back‑off</li></ul> | 99.9 % uptime over 30‑day period |
| **NFR‑4** | Usability | <ul><li>First‑time user walkthrough (3‑step)</li><li>Keyboard shortcuts for editor actions</li></ul> | User satisfaction > 4.5/5 in internal beta |
| **NFR‑5** | Maintainability | <ul><li>Code coverage ≥ 90 % for core modules</li><li>Documentation in Markdown + API docs (OpenAPI)</li></ul> | CI pipeline passes coverage checks |
| **NFR‑6** | Extensibility | <ul><li>LLM plug‑in interface defined in TypeScript</li><li>Metrics plug‑in system for custom evaluation</li></ul> | New LLM added in < 1 day by dev |
| **NFR‑7** | Internationalization | <ul><li>All static strings externalized in JSON</li><li>Right‑to‑left layout support</li></ul> | i18n test coverage 100 % |
| **NFR‑8** | Compliance | <ul><li>GDPR data handling (user consent, data erasure)</li><li>PCI‑DSS if cost data stored</li></ul> | Audit report from external firm |

---

## 4. Constraints

1. **Technology Stack**  
   - Frontend: React 18 + TypeScript + Vite  
   - Backend: Node.js 20 + Express + TypeScript  
   - Database: PostgreSQL 15 (primary) + Redis for caching  
   - LLM inference: vLLM or SGLang via Axentx shared BRAIN  
   - Containerization: Docker, orchestrated by Kubernetes (EKS)  

2. **Data Privacy**  
   - Prompt content may contain PII; must be stored encrypted and flagged for deletion upon user request.  

3. **Resource Limits**  
   - Compute budget capped at $5k/month for test runs; auto‑scale must respect this cap.  

4. **Deployment**  
   - Must deploy to Axentx’s existing CI/CD pipeline (GitHub Actions + ArgoCD).  

5. **Versioning**  
   - Semantic versioning for API; backward‑compatible changes only.  

---

## 5. Assumptions

- Users have access to at least one LLM model via Axentx’s inference engine.  
- The shared BRAIN contains up‑to‑date schema definitions for prompts and metrics.  
- Network latency between frontend and backend will not exceed 50 ms under normal load.  
- Legal review confirms that storing and processing prompt data complies with all applicable regulations.  

---

## 6. Deliverables

1. **Functional Specification** (this document)  
2. **API Design Docs** (OpenAPI v3)  
3. **Database Schema** (ER diagram + migration scripts)  
4. **Test Plan** (unit, integration, load, security)  
5. **Deployment Guide** (K8s manifests, Helm charts)  
6. **User Documentation** (help pages, video walkthrough)  

---

## 7. Acceptance Checklist

- [ ] All functional requirements implemented and unit‑tested.  
- [ ] Performance benchmarks meet NFR‑1.  
- [ ] Security audit passed.  
- [ ] 99.9 % uptime achieved in staging.  
- [ ] Documentation complete and reviewed.  
- [ ] Deployment pipeline fully automated.  

---
