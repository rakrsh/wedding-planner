from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import current_regular_user, get_db_session
from app.models.wedding import ProjectDetail, WeddingProject, ProjectStatus
from app.schemas.project import WeddingProjectCreate, WeddingProjectResponse, ProjectDetailPayload

router = APIRouter()

@router.get("/", response_model=List[WeddingProjectResponse])
def list_projects(db: Session = Depends(get_db_session), user=Depends(current_regular_user)):
    return db.query(WeddingProject).filter(WeddingProject.user_id == user["sub"]).all()

@router.post("/", response_model=WeddingProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(payload: WeddingProjectCreate, db: Session = Depends(get_db_session), user=Depends(current_regular_user)):
    project = WeddingProject(title=payload.title, user_id=user["sub"], status=ProjectStatus.DRAFT)
    db.add(project)
    db.flush()
    if payload.project_detail:
        detail = ProjectDetail(
            project_id=project.id,
            dates_config=payload.project_detail.dates_config,
            catering_config=payload.project_detail.catering_config,
            logistics_config=payload.project_detail.logistics_config,
            budget_config=payload.project_detail.budget_config,
        )
        db.add(detail)
    db.commit()
    db.refresh(project)
    return project

@router.get("/{project_id}", response_model=WeddingProjectResponse)
def get_project(project_id: UUID, db: Session = Depends(get_db_session), user=Depends(current_regular_user)):
    project = db.query(WeddingProject).filter(WeddingProject.id == project_id, WeddingProject.user_id == user["sub"]).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@router.post("/{project_id}/activate", response_model=WeddingProjectResponse)
def activate_project(project_id: UUID, db: Session = Depends(get_db_session), user=Depends(current_regular_user)):
    project = db.query(WeddingProject).filter(WeddingProject.id == project_id, WeddingProject.user_id == user["sub"]).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    project.status = ProjectStatus.ACTIVE
    db.commit()
    db.refresh(project)
    return project

@router.get("/{project_id}/export/json")
def export_project_json(project_id: UUID, db: Session = Depends(get_db_session), user=Depends(current_regular_user)):
    project = db.query(WeddingProject).filter(WeddingProject.id == project_id, WeddingProject.user_id == user["sub"]).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    detail = db.query(ProjectDetail).filter(ProjectDetail.project_id == project.id).first()
    return {
        "project": project,
        "details": detail,
    }
