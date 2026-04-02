import math

# forward difference derivative
def d(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

# functions + true derivatives
funcs = {
    "1": ("x²",  lambda x: x**2,        lambda x: 2*x),
    "2": ("x³",  lambda x: x**3,        lambda x: 3*x**2),
    "3": ("sin", math.sin,              math.cos),
    "4": ("cos", math.cos,              lambda x: -math.sin(x))
}

while True:
    print("===== CALCULATOR =====")
    print("1. Calculator\n2. Derivative\n3. Exit")

    c = input("Choose: ")

    if c == "3":
        print("Exiting.")
        break

    elif c == "1":
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))

            print(f"{a}+{b}={a+b}")
            print(f"{a}-{b}={a-b}")
            print(f"{a}*{b}={a*b}")
            print(f"{a}/{b}={a/b:.6f}" if b != 0 else "division by zero")

        except ValueError:
            print("Invalid input")

    elif c == "2":
        try:
            x = float(input("Enter x: "))

            for k, v in funcs.items():
                print(k, v[0])

            ch = input("Choose: ")

            if ch not in funcs:
                print("Invalid")
                continue

            name, f, true = funcs[ch]

            num = d(f, x)
            tv = true(x)

            print(f"\nf(x) = {name}, x = {x}")
            print(f"f(x) = {f(x):.6f}")
            print(f"num = {num:.6f}, true = {tv:.6f}")
            print(f"error = {abs(num - tv):.6f}")
            print("✓" if abs(num - tv) < 0.01 else "✗")

        except ValueError:
            print("Invalid input")

    else:
        print("Invalid choice")
