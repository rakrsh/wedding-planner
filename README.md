# wedding-planner

A highly scalable platform tailored specifically for the complex, multi-day, multi-vendor logistics of Indian weddings.

## Repository Structure

- `backend/`: FastAPI backend scaffold
- `infra/`: Docker Compose orchestration for PostgreSQL, MongoDB, Redis, Keycloak, and API service
- `docs/`: architecture and design documentation

## Getting Started

1. Build and launch services:

```bash
cd infra
docker compose up --build
```

2. API entrypoint:

```bash
http://localhost:8000/docs
```

## Architecture

- Identity: Keycloak OIDC / OAuth2 with JWT verification and role-based access control
- Relational data: PostgreSQL for wedding projects, venue geolocation, and workflow state
- Document data: MongoDB for invitation template serialization
- Async and export: Redis for brokered background tasks
