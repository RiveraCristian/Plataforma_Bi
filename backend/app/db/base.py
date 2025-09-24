from app.db.session import engine
from app.models.base import Base  # noqa: F401


def create_all() -> None:
    """Create all database tables."""

    Base.metadata.create_all(bind=engine)
