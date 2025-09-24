from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.dashboard import Dashboard, DashboardCreate
from app.schemas.dataset import Dataset, DatasetCreate
from app.schemas.field import Field, FieldCreate
from app.services.catalog.service import CatalogService

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.get("/datasets", response_model=List[Dataset])
def list_datasets(db: Session = Depends(get_db)):
    service = CatalogService(db)
    return service.list_datasets()


@router.post("/datasets", response_model=Dataset)
def create_dataset(dataset_in: DatasetCreate, db: Session = Depends(get_db)):
    service = CatalogService(db)
    return service.create_dataset(dataset_in)


@router.post("/fields", response_model=Field)
def add_field(field_in: FieldCreate, db: Session = Depends(get_db)):
    service = CatalogService(db)
    return service.add_field(field_in)


@router.post("/dashboards", response_model=Dashboard)
def create_dashboard(dashboard_in: DashboardCreate, db: Session = Depends(get_db)):
    service = CatalogService(db)
    return service.create_dashboard(dashboard_in)


@router.get("/dashboards", response_model=List[Dashboard])
def list_dashboards(db: Session = Depends(get_db)):
    service = CatalogService(db)
    return service.list_dashboards()
