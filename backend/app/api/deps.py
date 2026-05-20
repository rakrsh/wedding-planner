from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.security import require_admin, require_user, get_current_user
from app.db.session import get_db

def get_db_session() -> Generator[Session, None, None]:
    yield from get_db()

def current_user(user = Depends(get_current_user)):
    return user

def current_admin(user = Depends(require_admin)):
    return user

def current_regular_user(user = Depends(require_user)):
    return user
