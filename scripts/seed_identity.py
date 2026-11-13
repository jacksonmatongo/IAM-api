from iam_api.core.database import SessionLocal
from iam_api.modules.identity.services.seeder import seed_identity

def main():
    with SessionLocal.begin() as db:
        seed_identity(db)

    print("Identity seeding completed successfully.")

if __name__ == "__main__":
    main()