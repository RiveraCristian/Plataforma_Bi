from pydantic import BaseModel


class PermissionBase(BaseModel):
    user_id: int
    object_id: int
    object_type: str
    action: str


class PermissionCreate(PermissionBase):
    pass


class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True
