from sqlalchemy.orm import Session
from app.repositories.user_repository import user_repo
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, *, email: str, password: str, full_name: str | None = None):
    existing = user_repo.get_by_email(db, email)
    if existing:
        raise ValueError("Email already registered")
    hashed = hash_password(password)
    user = user_repo.create(db, {"email": email, "hashed_password": hashed, "full_name": full_name})
    return {"id": user.id, "email": user.email, "full_name": user.full_name}

def authenticate_user(db: Session, *, email: str, password: str) -> str | None:
    user = user_repo.get_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return create_access_token(str(user.id))
