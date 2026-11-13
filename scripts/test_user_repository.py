from iam_api.core.database import SessionLocal
from iam_api.modules.identity.repository.user_repository import create_user,get_user_by_email
from iam_api.modules.authentication.services.password import hash_password

def main():
    with SessionLocal.begin() as db:
        email="repository_tes@example.com"

        existing_user = get_user_by_email(db, email)

        if existing_user:
            print("Test user already exists.")
            return

        user = create_user(
            db,
            email=email,
            hashed_password = hash_password("TestPassword123!"),
            full_name="Repository Test",
        )

        print("User created successfully.")
        print(f"User ID: {user.id}")
        print(f"Email: {user.email}")

if __name__ == "__main__":
    main()