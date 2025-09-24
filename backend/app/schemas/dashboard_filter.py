from pydantic import BaseModel


class DashboardFilterBase(BaseModel):
    dashboard_id: int
    definition_json: dict


class DashboardFilterCreate(DashboardFilterBase):
    pass


class DashboardFilterUpdate(BaseModel):
    definition_json: dict | None = None


class DashboardFilter(DashboardFilterBase):
    id: int

    class Config:
        orm_mode = True
