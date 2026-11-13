
from sqlalchemy import select
from sqlalchemy.orm import Session

from iam_api.modules.identity.models import (
    Role,
    Permission,
    RolePermission,
)


INITIAL_ROLES = {
    "CLIENT": "A user who searches for properties.",
    "OWNER": "A property owner who lists properties.",
    "AGENT": "An agent who manages property listings.",
    "ADMIN": "An administrator who manages the platform.",
    "SUPER_ADMIN": "An administrator with full system privileges.",
}


INITIAL_PERMISSIONS = {
    "property:read": "View property listings.",
    "property:create": "Create property listings.",
    "property:update": "Update property listings.",
    "property:delete": "Delete property listings.",
    "user:read": "View user accounts.",
    "user:manage": "Manage user accounts.",
    "user:assign_role": "Assign roles to users.",
}


ROLE_PERMISSION_MAP = {
    "CLIENT": [
        "property:read",
    ],
    "OWNER": [
        "property:read",
        "property:create",
        "property:update",
    ],
    "AGENT": [
        "property:read",
        "property:create",
        "property:update",
    ],
    "ADMIN": [
        "property:read",
        "property:delete",
        "user:read",
        "user:manage",
    ],
    "SUPER_ADMIN": list(INITIAL_PERMISSIONS.keys()),
}

def seed_roles(db: Session) -> dict[str, Role]:
    roles = {}

    for name, description in INITIAL_ROLES.items():

        role = db.scalar(
            select(Role).where(Role.name == name)
        )

        if role is None:
            role = Role(
                name=name,
                description=description,
            )

            db.add(role)

        roles[name] = role

    db.flush()
    return roles

def seed_permissions(db: Session) -> dict[str, Permission]:
    permissions = {}

    for name, description in INITIAL_PERMISSIONS.items():

        permission = db.scalar(
            select(Permission).where(Permission.name == name)
        )

        if permission is None:
            permission = Permission(
                name=name,
                description=description,
            )

            db.add(permission)
        permissions[name] = permission
    db.flush()

    return permissions

def seed_role_permissions(
    db: Session,
    roles: dict[str, Role],
    permissions: dict[str, Permission]
    ) -> None:

    for role_name, permission_names in ROLE_PERMISSION_MAP.items():
        role = roles[role_name]

        for permission_name in permission_names:

            permission = permissions[permission_name]

            existing_assignment = db.scalar(
                select(RolePermission).where(RolePermission.role_id==role.id,
                RolePermission.permission_id == permission.id,)
            )

            if existing_assignment is None:
                assignment = RolePermission(
                    role_id=role.id,
                    permission_id=permission.id,
                )
                db.add(assignment)
    db.flush()

def seed_identity(db: Session) -> None:
    roles = seed_roles(db)

    permissions = seed_permissions(db)

    seed_role_permissions(
        db=db,
        roles=roles,
        permissions=permissions,
    )