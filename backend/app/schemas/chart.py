from typing import List

from pydantic import BaseModel, Field

from app.schemas.metric import Metric


class ChartBase(BaseModel):
    dashboard_id: int
    dataset_id: int
    config_json: dict


class ChartCreate(ChartBase):
    metric_ids: List[int]


class ChartUpdate(BaseModel):
    config_json: dict | None = None
    metric_ids: List[int] | None = None


class Chart(ChartBase):
    id: int
    metrics: List[Metric] = Field(default_factory=list)

    class Config:
        orm_mode = True
