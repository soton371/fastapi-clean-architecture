from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.schemas.user import UserCreate, UserOut
from app.services.user_service import register_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, email=user.email, password=user.password, full_name=user.full_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
