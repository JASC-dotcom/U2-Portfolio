# Jose Antonio Santiago Cabrera - act03_loops.py

# 1. Countdown (while)
n = int(input("n: "))
while n >= 0:
    end = ", " if n > 0 else "\n"
    print(n, end=end)
    n -= 1

# 2. Sum and average with sentinel (0 ends the input)
total = 0
count = 0
number = float(input("Number (0 to finish): "))
while number != 0:
    total += number
    count += 1
    number = float(input("Number (0 to finish): "))

if count > 0:
    print(f"Sum: {total} | Average: {total / count:.2f}")
else:
    print("No numbers were typed")

# 3. Multiplication table (for)
table = int(input("Table of: "))
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")

# 4. Port validation
port = int(input("Port (1-65535): "))
while not 1 <= port <= 65535:
    port = int(input("Invalid. Port again (1-65535): "))
print(f"Port {port} accepted")