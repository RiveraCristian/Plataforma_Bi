from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    expression = Column(Text, nullable=False)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    version = Column(Integer, default=1, nullable=False)

    dataset = relationship("Dataset", back_populates="metrics")
