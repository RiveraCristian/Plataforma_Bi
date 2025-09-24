from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):
    name: str
    email: EmailStr
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
