from typing import List

from pydantic import BaseModel


class QueryRequest(BaseModel):
    dataset_id: int
    metric_ids: List[int]
    dimensions: List[str] | None = None
