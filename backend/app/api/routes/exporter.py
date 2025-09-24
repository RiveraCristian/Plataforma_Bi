from fastapi import APIRouter

from app.services.exporter.service import ExporterService

router = APIRouter(prefix="/export", tags=["export"])
service = ExporterService()


@router.post("/dashboards/{dashboard_id}")
def export_dashboard(dashboard_id: int, export_type: str = "pdf"):
    path = service.export_dashboard(dashboard_id, export_type)
    return {"path": str(path)}
