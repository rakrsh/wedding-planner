# Wedding Planner Architecture

## System Overview

- Frontend: React / Next.js (planned)
- API: FastAPI
- Relational Database: PostgreSQL
- Document Store: MongoDB
- IAM: Keycloak (OIDC / OAuth2 with PKCE)
- Broker: Redis + Celery
- PDF Engine: WeasyPrint (async export)

## Polyglot Persistence

- `wedding_projects` (PostgreSQL): Project metadata, owner mappings, workflow state.
- `project_details` (PostgreSQL): JSONB payloads for draft configuration, dates, catering, logistics, and budget.
- `venues` (PostgreSQL): High-precision coordinates, address data, and Google Place IDs.
- `invitation_templates` (MongoDB): Schemaless canvas serialization for invitation and card designs.

## Workflow & Access Control

- `DRAFT` state allows incremental saving with relaxed validation.
- `ACTIVE` state enforces business rules and stable payloads.
- JWT verification is performed against Keycloak JWKS.
- RBAC roles supported: `ROLE_ADMIN`, `ROLE_USER`.

## Services

- `api`: FastAPI-based backend serving project CRUD, venue management, and invitation template storage.
- `postgres`: Transactional data store.
- `mongo`: Document database for canvas templates.
- `redis`: Broker for asynchronous tasks.
- `keycloak`: Identity provider for centralized SSO and token issuance.

## Local Run

```bash
cd infra
docker compose up --build
```
