from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from iam_api.core.database import Base

if TYPE_CHECKING:
    from iam_api.modules.identity.models.permission import Permission
    from iam_api.modules.identity.models.role import Role


class RolePermission(Base):
    __tablename__="role_permissions"

    __table_args__=(
        UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permissions_role_permission",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid7,
    )

    role_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    permission_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("permissions.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    role: Mapped[Role] = relationship(
        back_populates="permission_assignments"
    )

    permission: Mapped[Permission] = relationship(
        back_populates="role_assignment"
    )