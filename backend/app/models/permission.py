from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    object_id = Column(Integer, nullable=False)
    object_type = Column(String, nullable=False)
    action = Column(String, nullable=False)

    user = relationship("User", back_populates="permissions")
