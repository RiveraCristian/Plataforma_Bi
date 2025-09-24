from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str
    configuration: dict | None = None


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    name: str | None = None
    configuration: dict | None = None


class Organization(OrganizationBase):
    id: int

    class Config:
        orm_mode = True
