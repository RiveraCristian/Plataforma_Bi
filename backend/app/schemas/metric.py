from pydantic import BaseModel


class MetricBase(BaseModel):
    name: str
    expression: str
    dataset_id: int


class MetricCreate(MetricBase):
    pass


class MetricUpdate(BaseModel):
    name: str | None = None
    expression: str | None = None


class Metric(MetricBase):
    id: int
    version: int

    class Config:
        orm_mode = True
