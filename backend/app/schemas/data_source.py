from pydantic import BaseModel


class DataSourceBase(BaseModel):
    type: str
    connection_json: dict


class DataSourceCreate(DataSourceBase):
    pass


class DataSourceUpdate(BaseModel):
    connection_json: dict | None = None


class DataSource(DataSourceBase):
    id: int

    class Config:
        orm_mode = True
