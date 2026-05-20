import enum
import uuid
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.sql import func

from app.db.base import Base

class ProjectStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"

class WeddingProject(Base):
    __tablename__ = "wedding_projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(128), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    status = Column(Enum(ProjectStatus), nullable=False, default=ProjectStatus.DRAFT)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class ProjectDetail(Base):
    __tablename__ = "project_details"

    project_id = Column(UUID(as_uuid=True), ForeignKey("wedding_projects.id"), primary_key=True)
    dates_config = Column(JSONB, nullable=True)
    catering_config = Column(JSONB, nullable=True)
    logistics_config = Column(JSONB, nullable=True)
    budget_config = Column(JSONB, nullable=True)

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=True)
    latitude = Column(Numeric(10, 8), nullable=False)
    longitude = Column(Numeric(11, 8), nullable=False)
    google_place_id = Column(String(255), nullable=True, unique=True)
