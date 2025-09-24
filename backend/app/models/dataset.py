from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    source_id = Column(Integer, ForeignKey("data_sources.id"), nullable=False)
    sql_text = Column(Text, nullable=False)

    source = relationship("DataSource", backref="datasets")
    fields = relationship("Field", back_populates="dataset", cascade="all, delete-orphan")
    metrics = relationship("Metric", back_populates="dataset", cascade="all, delete-orphan")
    charts = relationship("Chart", back_populates="dataset")
