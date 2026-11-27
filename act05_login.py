# Jose Antonio Santiago Cabrera - act05_login.py

USER, PASSWORD = "admin", "asir2026"
MAX_TRIES = 3

attempts = 0
while attempts < MAX_TRIES:
    user = input("User: ").strip()
    pwd = input("Password: ").strip()

    if user == "" or pwd == "":
        print("Empty input ignored (it does not count)")
        continue

    if user == USER and pwd == PASSWORD:
        print("Access granted")
        break

    attempts += 1
    print(f"Wrong credentials. Attempts left: {MAX_TRIES - attempts}")
else:
    print("Account locked / Cuenta bloqueada")