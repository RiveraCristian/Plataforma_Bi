from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.data_source import DataSource, DataSourceCreate
from app.services.connectors.service import ConnectorService

router = APIRouter(prefix="/connectors", tags=["connectors"])


@router.post("/sources", response_model=DataSource)
def register_source(data_source_in: DataSourceCreate, db: Session = Depends(get_db)):
    service = ConnectorService(db)
    return service.register_data_source(data_source_in)
