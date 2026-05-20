from functools import lru_cache
from datetime import datetime
from typing import Dict, List, Optional

import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

from app.core.config import settings

security_scheme = HTTPBearer()

class TokenPayload:
    sub: str
    roles: List[str]
    exp: int

@lru_cache()
def get_jwks() -> Dict:
    response = requests.get(str(settings.keycloak_jwks_url), timeout=5)
    response.raise_for_status()
    return response.json()

def decode_jwt(token: str) -> Dict:
    jwks = get_jwks()
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")
    key = next((key for key in jwks.get("keys", []) if key.get("kid") == kid), None)
    if not key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token header")
    try:
        payload = jwt.decode(
            token,
            key,
            algorithms=[key.get("alg", "RS256")],
            audience=settings.oauth_audience,
        )
        return payload
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token validation failed") from exc

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)) -> Dict:
    token = credentials.credentials
    payload = decode_jwt(token)
    if payload.get("exp") and datetime.utcfromtimestamp(payload["exp"]) < datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    return {
        "sub": payload.get("sub"),
        "roles": payload.get("roles", []),
        "preferred_username": payload.get("preferred_username"),
    }

def require_role(role: str):
    def role_checker(user: Dict = Depends(get_current_user)):
        if role not in user["roles"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        return user
    return role_checker

require_admin = require_role("ROLE_ADMIN")
require_user = require_role("ROLE_USER")
