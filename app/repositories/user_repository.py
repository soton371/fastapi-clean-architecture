from sqlalchemy.orm import Session
from app.repositories.base import Repository
from app.models.user import User

class UserRepository(Repository[User]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

user_repo = UserRepository()
