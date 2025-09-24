from fastapi import APIRouter

from app.services.scheduler.service import SchedulerService

router = APIRouter(prefix="/scheduler", tags=["scheduler"])
service = SchedulerService()


@router.post("/refresh/{dataset_id}")
def schedule_refresh(dataset_id: int):
    task_id = service.schedule_refresh(dataset_id)
    return {"task_id": task_id}
