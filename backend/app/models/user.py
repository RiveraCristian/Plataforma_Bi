from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    role = Column(String, nullable=False)
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    hashed_password = Column(String, nullable=False)

    organization = relationship("Organization", backref="users")
    permissions = relationship("Permission", back_populates="user", cascade="all, delete-orphan")
