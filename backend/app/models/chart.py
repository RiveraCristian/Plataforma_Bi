from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.models.base import Base


class Chart(Base):
    __tablename__ = "charts"

    id = Column(Integer, primary_key=True, index=True)
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"), nullable=False)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    config_json = Column(JSON, nullable=False)

    dashboard = relationship("Dashboard", back_populates="charts")
    dataset = relationship("Dataset", back_populates="charts")
    metrics = relationship("ChartMetric", back_populates="chart", cascade="all, delete-orphan")
