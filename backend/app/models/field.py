from enum import Enum

from sqlalchemy import Column, Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class FieldRole(str, Enum):
    dimension = "dimension"
    measure = "measure"


class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    role = Column(SqlEnum(FieldRole), nullable=False)

    dataset = relationship("Dataset", back_populates="fields")
