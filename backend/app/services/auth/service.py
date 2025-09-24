from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.permission import Permission
from app.models.user import User
from app.schemas.user import UserCreate


class AuthService:
    """Handle authentication and authorization logic."""

    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_in: UserCreate) -> User:
        if self.db.query(User).filter(User.email == user_in.email).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        db_user = User(
            name=user_in.name,
            email=user_in.email,
            role=user_in.role,
            org_id=user_in.org_id,
            hashed_password=get_password_hash(user_in.password),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def authenticate(self, email: str, password: str) -> str:
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_access_token({"sub": str(user.id)}, expires_delta=timedelta(hours=8))

    def assign_permission(self, user_id: int, object_id: int, object_type: str, action: str) -> Permission:
        permission = Permission(user_id=user_id, object_id=object_id, object_type=object_type, action=action)
        self.db.add(permission)
        self.db.commit()
        self.db.refresh(permission)
        return permission

    def check_permission(self, user: User, object_id: int, object_type: str, action: str) -> bool:
        if user.role == "admin":
            return True
        return (
            self.db.query(Permission)
            .filter(
                Permission.user_id == user.id,
                Permission.object_id == object_id,
                Permission.object_type == object_type,
                Permission.action == action,
            )
            .first()
            is not None
        )
