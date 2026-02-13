import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

SALT_FILE = "salt.bin"
PW_FILE = "password.txt"

def load_or_create_salt():
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        return salt
    with open(SALT_FILE, "rb") as f:
        return f.read()

def derive_fernet_key(master_pwd: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))

def add(fer):
    name = input("Account name: ").strip()
    pwd = input("Password: ").strip()

    token = fer.encrypt(pwd.encode()).decode()

    with open(PW_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name}|{token}\n")

def view(fer):
    if not os.path.exists(PW_FILE):
        print("Ingen passwords gemt endnu.")
        return

    with open(PW_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                user, token = line.split("|", 1)
                user = user.strip()
                token = token.strip()
                pwd = fer.decrypt(token.encode()).decode()
                print(f"User: {user} | Password: {pwd}")
            except Exception:
                print("Kunne ikke læse en linje (forkert format eller forkert master password).")

def main():
    master_pwd = input("What is the master password? ")
    salt = load_or_create_salt()
    key = derive_fernet_key(master_pwd, salt)
    fer = Fernet(key)

    while True:
        mode = input("Add or view? (add/view) - press q to quit: ").lower().strip()

        if mode == "q":
            break
        elif mode == "add":
            add(fer)
        elif mode == "view":
            view(fer)
        else:
            print("Invalid mode")

    print("Goodbye!")

if __name__ == "__main__":
    main()
