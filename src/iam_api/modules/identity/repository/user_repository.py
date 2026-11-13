from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iam_api.modules.identity.models.user import User

def get_user_by_email(db: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return db.scalar(statement)

def get_user_by_id(db: Session, user_id: UUID) -> User | None:
    statement = select(User).where(User.id == user_id)
    return db.scalar(statement)

def create_user(
    db: Session,
    *,
    email: str,
    hashed_password: str,
    full_name: str,
    phone: str | None = None,
    ) -> User:
    user = User(
        email=email,
        password_hash=hashed_password,
        full_name=full_name,
        phone=phone,
    )

    db.add(user)
    db.flush()

    return user