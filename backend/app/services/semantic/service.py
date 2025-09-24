from sqlalchemy.orm import Session

from app.models.field import Field
from app.models.metric import Metric
from app.models.field import FieldRole
from app.schemas.field import FieldCreate
from app.schemas.metric import MetricCreate


class SemanticService:
    """Define metrics and dimensions for datasets."""

    def __init__(self, db: Session):
        self.db = db

    def create_metric(self, metric_in: MetricCreate) -> Metric:
        metric = Metric(**metric_in.dict())
        self.db.add(metric)
        self.db.commit()
        self.db.refresh(metric)
        return metric

    def create_dimension(self, field_in: FieldCreate) -> Field:
        payload = field_in.dict()
        payload["role"] = FieldRole.dimension
        field = Field(**payload)
        self.db.add(field)
        self.db.commit()
        self.db.refresh(field)
        return field

    def version_metric(self, metric_id: int, new_expression: str) -> Metric:
        metric = self.db.query(Metric).filter(Metric.id == metric_id).first()
        if metric is None:
            raise ValueError("Metric not found")
        new_metric = Metric(
            name=metric.name,
            expression=new_expression,
            dataset_id=metric.dataset_id,
            version=metric.version + 1,
        )
        self.db.add(new_metric)
        self.db.commit()
        self.db.refresh(new_metric)
        return new_metric
