# Numerical Derivative using Central Difference Method
# Formula used: (f(x + h) - f(x - h)) / (2*h)
# This gives a more accurate slope approximation than forward difference

# Function to compute numerical derivative
def numerical_derivative(f, x, h=0.001):
    # Uses values on both sides of x → reduces error
    return (f(x + h) - f(x - h)) / (2*h)

# Function: f(x) = x^2
# True derivative: f'(x) = 2x
def f_squared(x):
    return x**2

# Function: f(x) = x^3
# True derivative: f'(x) = 3x^2
def f_cubed(x):
    return x**3

# Print table header (aligned formatting)
print(f"{'num x²':>10} | {'true x²':>10} | {'match':>6} | {'num x³':>10} | {'true x³':>10} | {'match':>6}")
print("-" * 75)

# Loop through x values from -4 to 4
for x in range(-4, 5):

    # Compute numerical derivatives
    num_sq  = numerical_derivative(f_squared, x)
    num_cu  = numerical_derivative(f_cubed, x)

    # Compute true derivatives using formulas
    true_sq = 2 * x          # derivative of x^2
    true_cu = 3 * x**2       # derivative of x^3

    # Check if numerical result is close to true value (tolerance = 0.01)
    match_sq = "✓" if abs(num_sq - true_sq) < 0.01 else "✗"
    match_cu = "✓" if abs(num_cu - true_cu) < 0.01 else "✗"

    # Print formatted row for each x
    print(f"{num_sq:>10.4f} | {true_sq:>10.4f} | {match_sq:>6} | {num_cu:>10.4f} | {true_cu:>10.4f} | {match_cu:>6}")