from iam_api.modules.authentication.services.password import hash_password, verify_password

def main():
    password = "Jackson@2026"

    hashed = hash_password(password)

    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")

    print(f"Correct password: {verify_password("Jackson@2026", hashed)}")

    print(f"Incorrect password: {verify_password("Jackson!", hashed)}")

if __name__ == "__main__":
    main()