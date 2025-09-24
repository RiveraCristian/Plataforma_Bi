from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.query import QueryRequest
from app.services.query.service import QueryEngine

router = APIRouter(prefix="/query", tags=["query"])


@router.post("/execute")
def execute_query(payload: QueryRequest, db: Session = Depends(get_db)):
    service = QueryEngine(db)
    return service.execute(dataset_id=payload.dataset_id, metric_ids=payload.metric_ids, dimensions=payload.dimensions)
