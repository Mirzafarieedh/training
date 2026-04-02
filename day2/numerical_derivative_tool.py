def f(x):
    return x**2

# The derivative function
def numerical_derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

# Test on x²
print("Testing on f(x) = x²")

print(f"slope at x=1 → {numerical_derivative(f, 1):.4f}  (true: 2)")
print(f"slope at x=3 → {numerical_derivative(f, 3):.4f}  (true: 6)")
print(f"slope at x=5 → {numerical_derivative(f, 5):.4f}  (true: 10)")




        
