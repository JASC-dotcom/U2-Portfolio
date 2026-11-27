# Jose Antonio Santiago Cabrera - act02_menu.py

print("1) Disk 2) Users 3) Ping q) Quit")
option = input("> ").strip().lower()

match option:
    case "1":
        used = int(input("Used %: "))
        if used > 90:
            print("CRITICAL: disk almost full")
        elif used > 80:
            print("WARNING: disk usage is high")
        else:
            print("OK: disk usage is normal")
    case "2":
        print("Users: root, admin, jose (simulated)")
    case "3":
        ip = input("IP: ").strip()
        if len(ip.split(".")) != 4:
            print("Invalid IP: it must have 4 parts")
        else:
            print(f"Pinging {ip}... 4 packets received (simulated)")
    case "q":
        print("Bye!")
    case _:
        print("Unknown option")