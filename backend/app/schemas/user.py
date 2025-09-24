from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    role: str
    org_id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    role: str | None = None
    password: str | None = None


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
