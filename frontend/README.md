# Frontend (React + Vite)

This is a minimal React (Vite) scaffold for the Indian Wedding Planner UI.

Run locally:

```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:5173

Notes:
- The pages call the backend at `http://localhost:8000`.
- To interact with protected endpoints (e.g., `/projects`) supply a Keycloak access token in the Projects page.

Production build (Docker):

```bash
cd frontend
docker build -t wedding-planner-frontend:latest .
docker run --rm -p 8080:80 --name wedding-frontend wedding-planner-frontend:latest
```

Open: http://localhost:8080

Notes:
- The included `nginx.conf` adds an `/api` proxy to `http://api:8000/` which is useful when running inside the Docker Compose network. If you use the container standalone, either remove the proxy or run the API container and connect them on the same network.
