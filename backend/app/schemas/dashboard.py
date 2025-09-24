from typing import List

from pydantic import BaseModel, Field

from app.schemas.chart import Chart
from app.schemas.dashboard_filter import DashboardFilter


class DashboardBase(BaseModel):
    name: str
    owner_id: int
    layout_json: dict
    description: str | None = None


class DashboardCreate(DashboardBase):
    pass


class DashboardUpdate(BaseModel):
    name: str | None = None
    layout_json: dict | None = None


class Dashboard(DashboardBase):
    id: int
    version: int
    charts: List[Chart] = Field(default_factory=list)
    filters: List[DashboardFilter] = Field(default_factory=list)

    class Config:
        orm_mode = True
