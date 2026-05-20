from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo import MongoClient
from pydantic import BaseModel

from app.core.config import settings
from app.api.deps import current_regular_user

client = MongoClient(settings.mongo_url)
db = client.get_database("wedding")
collection = db.get_collection("invitation_templates")

class InvitationCreate(BaseModel):
    project_id: str
    asset_type: str
    dimensions: dict
    layers: list
    status: str = "DRAFT"

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_invitation(payload: InvitationCreate, user=Depends(current_regular_user)):
    record = payload.dict()
    record["created_by"] = user["sub"]
    result = collection.insert_one(record)
    record["id"] = str(result.inserted_id)
    return record

@router.get("/", response_model=List[InvitationCreate])
def list_invitations(project_id: str = None, user=Depends(current_regular_user)):
    query = {"created_by": user["sub"]}
    if project_id:
        query["project_id"] = project_id
    results = list(collection.find(query))
    for item in results:
        item["id"] = str(item.pop("_id"))
    return results
