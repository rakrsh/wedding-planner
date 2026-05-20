from pydantic import BaseSettings, AnyUrl

class Settings(BaseSettings):
    app_name: str = "Indian Wedding Planner API"
    environment: str = "development"

    database_url: str = "postgresql+psycopg2://postgres:postgres@postgres:5432/wedding"
    mongo_url: str = "mongodb://mongo:27017"
    redis_url: str = "redis://redis:6379/0"

    keycloak_jwks_url: AnyUrl = "http://keycloak:8080/auth/realms/wedding-planner/protocol/openid-connect/certs"
    oauth_audience: str = "wedding-planner-api"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
