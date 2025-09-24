from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.models.base import Base


class Dashboard(Base):
    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String, nullable=True)
    layout_json = Column(JSON, nullable=False)
    version = Column(Integer, default=1, nullable=False)

    owner = relationship("User", backref="dashboards")
    charts = relationship("Chart", back_populates="dashboard", cascade="all, delete-orphan")
    filters = relationship("DashboardFilter", back_populates="dashboard", cascade="all, delete-orphan")
