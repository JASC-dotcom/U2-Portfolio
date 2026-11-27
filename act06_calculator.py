# Jose Antonio Santiago Cabrera - act06_calculator.py

import math

operations = 0

while True:
    op = input("Operation (+ - * / q): ").strip().lower()
    if op == "q":
        break
    if op not in ("+", "-", "*", "/"):
        print("Unknown operation, try + - * / or q")
        continue

    try:
        a = float(input("a: "))
        b = float(input("b: "))
        if not (math.isfinite(a) and math.isfinite(b)):
            raise ValueError("number too large or not finite")

        match op:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
            case "/":
                result = a / b
    except ValueError:
        print("Please type valid numbers (use a point, not a comma)")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        if math.isfinite(result):
            print(f"Result: {result:.2f}")
        else:
            print("The result is too large")
    finally:
        operations += 1

print(f"Operations attempted: {operations}")