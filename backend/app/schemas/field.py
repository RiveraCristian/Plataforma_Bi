from pydantic import BaseModel

from app.models.field import FieldRole


class FieldBase(BaseModel):
    dataset_id: int
    name: str
    type: str
    role: FieldRole = FieldRole.dimension


class FieldCreate(FieldBase):
    pass


class FieldUpdate(BaseModel):
    name: str | None = None
    type: str | None = None
    role: FieldRole | None = None


class Field(FieldBase):
    id: int

    class Config:
        orm_mode = True
