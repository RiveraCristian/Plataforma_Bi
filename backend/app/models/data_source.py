from sqlalchemy import Column, Integer, JSON, String

from app.models.base import Base


class DataSource(Base):
    __tablename__ = "data_sources"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    connection_json = Column(JSON, nullable=False)
