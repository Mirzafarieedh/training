

import math

# Allowed functions for safety
allowed = {
    "x": 0,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "exp": math.exp,
    "log": math.log,
    "sqrt": math.sqrt
}

def f(expr, x):
    allowed["x"] = x
    return eval(expr, {"__builtins__": {}}, allowed)

def derivative(expr, x, h=1e-5):
    return (f(expr, x + h) - f(expr, x)) / h

# ===== INPUT =====
expr = input("Enter function in x (e.g. x**2, sin(x)): ")
x = float(input("Enter value of x: "))

# ===== OUTPUT =====
slope = derivative(expr, x)
print(f"Slope at x = {x} is approximately: {slope}")




        