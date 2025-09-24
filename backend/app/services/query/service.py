from __future__ import annotations

from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.core.cache import cache_result, get_cached_result
from app.models.dataset import Dataset
from app.models.metric import Metric


class QueryEngine:
    """Build and execute queries based on semantic definitions."""

    def __init__(self, db: Session):
        self.db = db

    def build_query(self, dataset: Dataset, metric_ids: List[int], dimensions: List[str] | None = None) -> str:
        metrics = self.db.query(Metric).filter(Metric.id.in_(metric_ids)).all()
        if not metrics:
            raise ValueError("No metrics provided")
        select_clauses = [metric.expression + f" AS {metric.name}" for metric in metrics]
        group_by_clauses: List[str] = []
        if dimensions:
            group_by_clauses = dimensions
            select_clauses.extend(dimensions)
        sql = f"SELECT {', '.join(select_clauses)} FROM ({dataset.sql_text}) AS base"
        if group_by_clauses:
            sql += f" GROUP BY {', '.join(group_by_clauses)}"
        return sql

    def execute(self, dataset_id: int, metric_ids: List[int], dimensions: List[str] | None = None) -> Dict[str, Any]:
        dataset = self.db.query(Dataset).filter(Dataset.id == dataset_id).first()
        if dataset is None:
            raise ValueError("Dataset not found")
        cache_key = f"query:{dataset_id}:{','.join(map(str, metric_ids))}:{','.join(dimensions or [])}"
        cached = get_cached_result(cache_key)
        if cached is not None:
            return cached
        sql = self.build_query(dataset, metric_ids, dimensions)
        # Placeholder for actual query execution
        result = {"sql": sql, "data": []}
        cache_result(cache_key, result)
        return result
