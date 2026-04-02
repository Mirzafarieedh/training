import math

# ── core functions ──────────────────────────────────────────

def numerical_derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

# ── math functions ──────────────────────────────────────────

def f_squared(x): return x**2
def f_cubed(x):   return x**3
def f_sin(x):     return math.sin(x)
def f_cos(x):     return math.cos(x)

FUNCTIONS = {
    "1": ("x²",  f_squared,  "2x"),
    "2": ("x³",  f_cubed,    "3x²"),
    "3": ("sin", f_sin,      "cos(x)"),
    "4": ("cos", f_cos,      "-sin(x)"),
}

# ── calculator ──────────────────────────────────────────────

def calculator(a, b):
    print(f"\n  {a} + {b} = {a + b}")
    print(f"  {a} - {b} = {a - b}")
    print(f"  {a} * {b} = {a * b}")
    if b != 0:
        print(f"  {a} / {b} = {a / b:.6f}")
    else:
        print(f"  {a} / {b} = undefined (division by zero)")

# ── derivative ──────────────────────────────────────────────

def derivative_option(x):
    print("\n  Which function?")
    for key, (name, _, _) in FUNCTIONS.items():
        print(f"    {key}. {name}")
    
    choice = input("  Choose (1-4): ").strip()
    
    if choice not in FUNCTIONS:
        print("  Invalid choice.")
        return
    
    name, f, true_formula = FUNCTIONS[choice]
    
    numerical = numerical_derivative(f, x)
    
    # compute true value for verification
    if choice == "1":   true_val = 2 * x
    elif choice == "2": true_val = 3 * x**2
    elif choice == "3": true_val = math.cos(x)
    elif choice == "4": true_val = -math.sin(x)
    
    print(f"\n  Function : f(x) = {name}")
    print(f"  At x     : {x}")
    print(f"  f(x)     : {f(x):.6f}")
    print(f"  Numerical derivative : {numerical:.6f}")
    print(f"  True formula ({true_formula}) : {true_val:.6f}")
    print(f"  Error    : {abs(numerical - true_val):.8f}")
    
    match = "✓ match" if abs(numerical - true_val) < 0.01 else "✗ mismatch"
    print(f"  Result   : {match}")

# ── main CLI ────────────────────────────────────────────────

def main():
    print("=" * 40)
    print("       CALCULATOR    ")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("  1. Calculator (+, -, *, /)")
        print("  2. Derivative at a point")
        print("  3. Exit")
        
        choice = input("\nChoose (1-3): ").strip()
        
        if choice == "1":
            try:
                a = float(input("  Enter a: "))
                b = float(input("  Enter b: "))
                calculator(a, b)
            except ValueError:
                print("  Enter valid numbers.")
        
        elif choice == "2":
            try:
                x = float(input("  Enter x: "))
                derivative_option(x)
            except ValueError:
                print("  Enter a valid number.")
        
        elif choice == "3":
            print("Exiting.")
            break
        
        else:
            print("  Invalid. Choose 1, 2, or 3.")

main()