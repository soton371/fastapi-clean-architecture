from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, Any

ModelType = TypeVar("ModelType")

class Repository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.get(self.model, id)

    def get_by(self, db: Session, **filters):
        return db.query(self.model).filter_by(**filters).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: dict) -> ModelType:
        obj = self.model(**obj_in)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
