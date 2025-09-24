from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.field import Field, FieldCreate
from app.schemas.metric import Metric, MetricCreate
from app.services.semantic.service import SemanticService

router = APIRouter(prefix="/semantic", tags=["semantic"])


@router.post("/metrics", response_model=Metric)
def create_metric(metric_in: MetricCreate, db: Session = Depends(get_db)):
    service = SemanticService(db)
    return service.create_metric(metric_in)


@router.post("/dimensions", response_model=Field)
def create_dimension(field_in: FieldCreate, db: Session = Depends(get_db)):
    service = SemanticService(db)
    return service.create_dimension(field_in)
