from celery import Celery

from app.core.config import get_settings

settings = get_settings()

celery_app = Celery(
    "plataforma_bi",
    broker=settings.redis_url,
    backend=settings.redis_url,
)


@celery_app.task
def refresh_dataset(dataset_id: int) -> str:  # pragma: no cover - external service
    return f"Dataset {dataset_id} refreshed"


class SchedulerService:
    """Schedule background jobs such as dataset refresh."""

    def schedule_refresh(self, dataset_id: int) -> str:
        task = refresh_dataset.delay(dataset_id)
        return task.id
