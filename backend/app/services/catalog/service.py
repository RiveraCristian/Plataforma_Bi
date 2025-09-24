from typing import List

from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.models.field import Field
from app.models.dashboard import Dashboard
from app.schemas.dataset import DatasetCreate
from app.schemas.field import FieldCreate
from app.schemas.dashboard import DashboardCreate


class CatalogService:
    """Manage datasets, fields and dashboard metadata."""

    def __init__(self, db: Session):
        self.db = db

    def list_datasets(self) -> List[Dataset]:
        return self.db.query(Dataset).all()

    def create_dataset(self, dataset_in: DatasetCreate) -> Dataset:
        dataset = Dataset(**dataset_in.dict())
        self.db.add(dataset)
        self.db.commit()
        self.db.refresh(dataset)
        return dataset

    def add_field(self, field_in: FieldCreate) -> Field:
        field = Field(**field_in.dict())
        self.db.add(field)
        self.db.commit()
        self.db.refresh(field)
        return field

    def create_dashboard(self, dashboard_in: DashboardCreate) -> Dashboard:
        dashboard = Dashboard(
            name=dashboard_in.name,
            owner_id=dashboard_in.owner_id,
            layout_json=dashboard_in.layout_json,
            description=dashboard_in.description,
        )
        self.db.add(dashboard)
        self.db.commit()
        self.db.refresh(dashboard)
        return dashboard

    def list_dashboards(self) -> List[Dashboard]:
        return self.db.query(Dashboard).all()
