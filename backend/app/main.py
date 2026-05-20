from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import projects, venues, invitations

app = FastAPI(
    title="Indian Wedding Planner API",
    description="Polyglot backend scaffold for wedding logistics, venue mapping, and invitation templates.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(venues.router, prefix="/venues", tags=["venues"])
app.include_router(invitations.router, prefix="/invitations", tags=["invitations"])

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
