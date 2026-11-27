"""Mini admin console.

Author : Jose Antonio Santiago Cabrera
Date   : 2026-10-30
Version: 1.0
"""

USER, PASSWORD = "admin", "asir2026"
MAX_TRIES = 3
MAX_PORT = 65535
WELL_KNOWN_MAX = 1023
REGISTERED_MAX = 49151
MIN_PASSWORD_LENGTH = 8


def login():
    """Return True if the user logs in within MAX_TRIES attempts."""
    for attempt in range(1, MAX_TRIES + 1):
        user = input("User: ").strip()
        pwd = input("Password: ").strip()
        if user == USER and pwd == PASSWORD:
            print("Access granted")
            return True
        print(f"Wrong credentials. Attempts left: {MAX_TRIES - attempt}")
    print("Account locked / Cuenta bloqueada")
    return False


def read_int(prompt, low, high):
    """Ask until the user types a whole number between low and high."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That is not a whole number. Try again.")
            continue
        if low <= value <= high:
            return value
        print(f"Out of range ({low}-{high}). Try again.")


def port_classifier():
    port = read_int("Port: ", 1, MAX_PORT)
    if port <= WELL_KNOWN_MAX:
        kind = "WELL-KNOWN"
    elif port <= REGISTERED_MAX:
        kind = "REGISTERED"
    else:
        kind = "DYNAMIC"
    print(f"{port} is a {kind} port")


def password_checker():
    pwd = input("Password to check: ")
    has_digit = False
    has_upper = False
    for char in pwd:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    print(f"Length >= {MIN_PASSWORD_LENGTH}: {len(pwd) >= MIN_PASSWORD_LENGTH}")
    print(f"Has a digit: {has_digit}")
    print(f"Has an upper case letter: {has_upper}")
    if len(pwd) >= MIN_PASSWORD_LENGTH and has_digit and has_upper:
        print("Strong password")
    else:
        print("Weak password")


def backup_countdown():
    seconds = read_int("Seconds before backup (1-60): ", 1, 60)
    for second in range(seconds, 0, -1):
        print(f"Backup in {second}...")
    print("Backup completed")


def main():
    if not login():
        return

    while True:
        print("== ADMIN CONSOLE ==")
        print("1) Port 2) Password 3) Backup q) Quit")
        option = input("> ").strip().lower()

        match option:
            case "1":
                port_classifier()
            case "2":
                password_checker()
            case "3":
                backup_countdown()
            case "q":
                print("Bye!")
                break
            case _:
                print("Unknown option")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed by the user")