from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.dependencies import get_current_user_id
from app.repositories.user_repository import user_repo

router = APIRouter(prefix="/me", tags=["me"])

@router.get("")
def read_me(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    u = user_repo.get(db, user_id)
    return {"id": u.id, "email": u.email, "full_name": u.full_name} if u else {}
