# -----------------------------
# Function definition
# -----------------------------
def f(x):
    return x**2


# -----------------------------
# Derivative methods
# -----------------------------
def forward_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def central_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)


# -----------------------------
# Safe input handling
# -----------------------------
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


# -----------------------------
# Safe division
# -----------------------------
def safe_divide(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b


# -----------------------------
# Calculator block
# -----------------------------
print("=== Calculator ===")
a = get_float("Enter first number: ")
b = get_float("Enter second number: ")

print("\nResults:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {safe_divide(a, b)}")


# -----------------------------
# Limit / Derivative explorer
# -----------------------------
print("\n=== Derivative Explorer ===")
x = get_float("Enter x: ")

true_value = 2 * x

print(f"\nAt x = {x}")
print(f"{'h':<12}{'Forward':<15}{'Central':<15}{'True':<15}")

h_values = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]

for h in h_values:
    fwd = forward_derivative(f, x, h)
    cen = central_derivative(f, x, h)
    print(f"{h:<12.5f}{fwd:<15.6f}{cen:<15.6f}{true_value:<15.6f}")
