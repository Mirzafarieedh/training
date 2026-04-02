def numerical_derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

# Input any function + x, print slope
def my_function(x):
    return x**2   # change this to test different functions

x = float(input("Enter x: "))
slope = numerical_derivative(my_function, x)
print(f"Slope of f(x) at x={x} → {slope:.6f}")
