from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


class ChartMetric(Base):
    __tablename__ = "chart_metrics"

    id = Column(Integer, primary_key=True, index=True)
    chart_id = Column(Integer, ForeignKey("charts.id"), nullable=False)
    metric_id = Column(Integer, ForeignKey("metrics.id"), nullable=False)

    chart = relationship("Chart", back_populates="metrics")
    metric = relationship("Metric")
