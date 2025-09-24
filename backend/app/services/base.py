from sqlalchemy.orm import Session


class BaseService:
    """Base service providing access to the database session."""

    def __init__(self, db: Session):
        self.db = db
