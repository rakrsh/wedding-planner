from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

class ProjectStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"

class VenueCreate(BaseModel):
    name: str
    address: Optional[str]
    latitude: float
    longitude: float
    google_place_id: Optional[str]

class ProjectDetailPayload(BaseModel):
    dates_config: Optional[Dict[str, Any]] = Field(default_factory=dict)
    catering_config: Optional[Dict[str, Any]] = Field(default_factory=dict)
    logistics_config: Optional[Dict[str, Any]] = Field(default_factory=dict)
    budget_config: Optional[Dict[str, Any]] = Field(default_factory=dict)

class WeddingProjectCreate(BaseModel):
    title: str
    project_detail: Optional[ProjectDetailPayload] = None

class WeddingProjectResponse(BaseModel):
    id: UUID
    user_id: str
    title: str
    status: ProjectStatus

    class Config:
        orm_mode = True

class InvitationTemplatePayload(BaseModel):
    project_id: UUID
    asset_type: str
    dimensions: Dict[str, int]
    layers: List[Dict[str, Any]]
    status: str = "DRAFT"

class InvitationTemplateResponse(InvitationTemplatePayload):
    id: str
