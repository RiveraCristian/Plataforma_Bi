from typing import Dict, Type

from sqlalchemy.orm import Session

from app.models.data_source import DataSource
from app.schemas.data_source import DataSourceCreate


class BaseConnector:
    """Base class for connector drivers."""

    def test_connection(self, config: dict) -> bool:
        raise NotImplementedError


class PostgresConnector(BaseConnector):
    def test_connection(self, config: dict) -> bool:  # pragma: no cover - placeholder implementation
        required_keys = {"host", "port", "user", "password", "database"}
        return required_keys.issubset(config.keys())


class ConnectorService:
    """Manage data source connectors."""

    _drivers: Dict[str, Type[BaseConnector]] = {
        "postgres": PostgresConnector,
    }

    def __init__(self, db: Session):
        self.db = db

    def register_data_source(self, data_source_in: DataSourceCreate) -> DataSource:
        connector = self._drivers.get(data_source_in.type)
        if connector is None:
            raise ValueError(f"Unsupported connector type: {data_source_in.type}")
        driver = connector()
        if not driver.test_connection(data_source_in.connection_json):
            raise ValueError("Connection parameters are invalid")
        data_source = DataSource(**data_source_in.dict())
        self.db.add(data_source)
        self.db.commit()
        self.db.refresh(data_source)
        return data_source
