from pydantic import BaseModel


class DatasetBase(BaseModel):
    name: str
    source_id: int
    sql_text: str


class DatasetCreate(DatasetBase):
    pass


class DatasetUpdate(BaseModel):
    name: str | None = None
    sql_text: str | None = None


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True
