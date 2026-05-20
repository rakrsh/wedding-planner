from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import current_admin, get_db_session
from app.models.wedding import Venue
from app.schemas.project import VenueCreate

router = APIRouter()

@router.post("/", response_model=VenueCreate, status_code=status.HTTP_201_CREATED)
def create_venue(payload: VenueCreate, db: Session = Depends(get_db_session), user=Depends(current_admin)):
    venue = Venue(
        name=payload.name,
        address=payload.address,
        latitude=payload.latitude,
        longitude=payload.longitude,
        google_place_id=payload.google_place_id,
    )
    db.add(venue)
    db.commit()
    db.refresh(venue)
    return payload

@router.get("/", response_model=List[VenueCreate])
def list_venues(db: Session = Depends(get_db_session)):
    return db.query(Venue).all()

@router.get("/{venue_id}", response_model=VenueCreate)
def get_venue(venue_id: int, db: Session = Depends(get_db_session)):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not venue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venue not found")
    return venue
