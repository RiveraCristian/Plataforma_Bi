from sqlalchemy import Column, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship

from app.models.base import Base


class DashboardFilter(Base):
    __tablename__ = "filters"

    id = Column(Integer, primary_key=True, index=True)
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"), nullable=False)
    definition_json = Column(JSON, nullable=False)

    dashboard = relationship("Dashboard", back_populates="filters")
