from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import LoginRequest
from app.schemas.user import User, UserCreate
from app.services.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=User)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register_user(user_in)


@router.post("/token")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    access_token = service.authenticate(payload.username, payload.password)
    return {"access_token": access_token, "token_type": "bearer"}
